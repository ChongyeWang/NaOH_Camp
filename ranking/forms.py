from django import forms
from .models import Rating

class RankingForm(forms.ModelForm):
    name = forms.CharField(max_length=50)

    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Content"
        })
    )

    class Meta:
        model = Rating
        fields = ('name', 'body', )
