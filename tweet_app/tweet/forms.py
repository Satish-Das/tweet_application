from django import forms
from .models import Tweet, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control form-control-lg', 
                'rows': 4, 
                'placeholder': "What's happening? Share your thoughts...",
                'maxlength': 240,
                'style': 'border-radius: 12px; border: 2px solid var(--border-color); font-size: 1.1rem; padding: 1rem;',
                'oninput': 'updateCharCount(this)',
                'required': True
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
                'style': 'border-radius: 12px; border: 2px solid var(--border-color); padding: 0.8rem;',
                'onchange': 'previewImage(this)'
            })
        }
        
    def clean_text(self):
        text = self.cleaned_data.get('text')
        if not text or len(text.strip()) == 0:
            raise forms.ValidationError("Tweet text cannot be empty.")
        if len(text) > 240:
            raise forms.ValidationError("Tweet text cannot exceed 240 characters.")
        return text

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'birth_date', 'avatar', 'website']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }