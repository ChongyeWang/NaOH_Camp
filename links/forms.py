from django import forms
from .models import Link

class LinkForm(forms.ModelForm):
    name = forms.CharField(max_length=15)

    link = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Content"
        })
    )

    class Meta:
        model = Link
        fields = ('name', 'link', )
