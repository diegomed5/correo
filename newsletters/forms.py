from django import forms
from .models import NewsLetterUser, NewsLetter

class NewsLetterUserSignUpForm(forms.ModelForm):
    class Meta:
        model = NewsLetterUser
        fields = ['email']


class NewsLetterCreationForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['name', 'subject', 'body', 'email']