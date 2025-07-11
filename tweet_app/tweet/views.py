from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db import models
from django.contrib import messages
from .models import Tweet, UserProfile, Like, Comment, Report, Block
from .forms import TweetForm, UserRegistrationForm, UserProfileForm, UserUpdateForm, CommentForm, ReportForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_list")
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form}) 

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user = request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_view(request, username=None):
    if username:
        user = get_object_or_404(User, username=username)
    else:
        user = request.user
    
    profile, created = UserProfile.objects.get_or_create(user=user)
    tweets = Tweet.objects.filter(user=user).order_by('-created_at')
    
    context = {
        'profile_user': user,
        'profile': profile,
        'tweets': tweets,
        'is_own_profile': user == request.user,
    }
    return render(request, 'profile.html', context)

@login_required
def profile_edit(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile_view', username=request.user.username)
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'profile_edit.html', context)

@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    profile_to_follow, created = UserProfile.objects.get_or_create(user=user_to_follow)
    
    if user_to_follow != request.user:
        if request.user in profile_to_follow.followers.all():
            profile_to_follow.followers.remove(request.user)
        else:
            profile_to_follow.followers.add(request.user)
    
    return redirect('profile_view', username=username)

@login_required
def like_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    like, created = Like.objects.get_or_create(user=request.user, tweet=tweet)
    
    if not created:
        # If like already exists, remove it (unlike)
        like.delete()
        liked = False
    else:
        liked = True
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'liked': liked,
            'likes_count': tweet.likes_count
        })
    
    return redirect('tweet_list')

def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    comments = tweet.comments.all()
    
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.tweet = tweet
            comment.save()
            return redirect('tweet_detail', tweet_id=tweet.id)
    else:
        comment_form = CommentForm() if request.user.is_authenticated else None
    
    context = {
        'tweet': tweet,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'tweet_detail.html', context)

def search(request):
    query = request.GET.get('q', '')
    users = []
    tweets = []
    
    if query:
        # Search users by username, first name, or last name
        users = User.objects.filter(
            models.Q(username__icontains=query) |
            models.Q(first_name__icontains=query) |
            models.Q(last_name__icontains=query)
        ).distinct()[:10]  # Limit to 10 results
        
        # Search tweets by text content
        tweets = Tweet.objects.filter(
            text__icontains=query
        ).order_by('-created_at')[:20]  # Limit to 20 results
    
    context = {
        'query': query,
        'users': users,
        'tweets': tweets,
        'users_count': users.count() if users else 0,
        'tweets_count': tweets.count() if tweets else 0,
    }
    return render(request, 'search.html', context)

@login_required
def report_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    
    # Check if user has already reported this tweet
    if Report.objects.filter(reporter=request.user, tweet=tweet).exists():
        messages.warning(request, 'You have already reported this tweet.')
        return redirect('tweet_detail', tweet_id=tweet.id)
    
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.reporter = request.user
            report.tweet = tweet
            report.save()
            messages.success(request, 'Thank you for your report. We will review it shortly.')
            return redirect('tweet_detail', tweet_id=tweet.id)
    else:
        form = ReportForm()
    
    context = {
        'tweet': tweet,
        'form': form,
    }
    return render(request, 'report_tweet.html', context)

@login_required
def block_user(request, username):
    user_to_block = get_object_or_404(User, username=username)
    
    if user_to_block == request.user:
        messages.error(request, 'You cannot block yourself.')
        return redirect('profile_view', username=username)
    
    block, created = Block.objects.get_or_create(blocker=request.user, blocked=user_to_block)
    
    if created:
        messages.success(request, f'You have blocked @{user_to_block.username}.')
    else:
        # If block already exists, unblock
        block.delete()
        messages.success(request, f'You have unblocked @{user_to_block.username}.')
    
    return redirect('profile_view', username=username)

@login_required
def blocked_users(request):
    blocked_users = User.objects.filter(
        blocked_by__blocker=request.user
    ).order_by('-blocked_by__created_at')
    
    context = {
        'blocked_users': blocked_users,
    }
    return render(request, 'blocked_users.html', context)