from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    message = forms.CharField(label='Комментарий', widget=forms.Textarea(attrs={'class': 'form-control  required'}))

    class Meta:
        model = Post
        fields = ['message']
