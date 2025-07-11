from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),
    path('search/', views.search, name='search'),
    path('<int:tweet_id>/', views.tweet_detail, name='tweet_detail'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('<int:tweet_id>/like/', views.like_tweet, name='like_tweet'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/<str:username>/', views.profile_view, name='profile_view'),
    path('follow/<str:username>/', views.follow_user, name='follow_user'),
]
