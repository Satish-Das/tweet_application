from django.contrib import admin
from .models import Tweet, UserProfile, Like, Comment, Report, Block

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

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['reporter', 'tweet', 'report_type', 'status', 'created_at']
    list_filter = ['report_type', 'status', 'created_at']
    search_fields = ['reporter__username', 'tweet__text', 'description']
    actions = ['mark_as_reviewed', 'mark_as_resolved', 'mark_as_dismissed']
    
    def mark_as_reviewed(self, request, queryset):
        queryset.update(status='reviewed')
    mark_as_reviewed.short_description = "Mark selected reports as reviewed"
    
    def mark_as_resolved(self, request, queryset):
        queryset.update(status='resolved')
    mark_as_resolved.short_description = "Mark selected reports as resolved"
    
    def mark_as_dismissed(self, request, queryset):
        queryset.update(status='dismissed')
    mark_as_dismissed.short_description = "Mark selected reports as dismissed"

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ['blocker', 'blocked', 'created_at']
    list_filter = ['created_at']
    search_fields = ['blocker__username', 'blocked__username']