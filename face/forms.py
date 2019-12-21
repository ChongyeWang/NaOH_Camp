from django import forms
from .models import Face


class Photo(forms.ModelForm):
    image = forms.ImageField()    
    class Meta:
        model = Face
        fields = ('image', )