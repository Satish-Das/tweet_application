from django.contrib import admin
from .models import Tweet, UserProfile, Like, Comment

# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['text', 'user__username']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location', 'followers_count']
    search_fields = ['user__username', 'bio', 'location']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'tweet', 'reaction_type', 'created_at']
    list_filter = ['reaction_type', 'created_at']
    search_fields = ['user__username', 'tweet__text']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'tweet', 'text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'tweet__text', 'text']