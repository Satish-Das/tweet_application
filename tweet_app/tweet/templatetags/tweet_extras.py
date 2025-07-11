from django import template
from ..models import Like

register = template.Library()

@register.filter
def is_liked_by(tweet, user):
    """Check if a tweet is liked by a specific user"""
    if not user.is_authenticated:
        return False
    return Like.objects.filter(tweet=tweet, user=user).exists()
