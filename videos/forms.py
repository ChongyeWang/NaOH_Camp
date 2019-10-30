from django import forms
from .models import Post, Videos

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128)

    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "内容"
        })
    )

    class Meta:
        model = Post
        fields = ('title', 'body', )


class VideoForm(forms.ModelForm):
    video = forms.FileField(label='Video')    
    class Meta:
        model = Videos
        fields = ('video', )