from django import forms


class PostForm(forms.Form):
    
    q1 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "法国的特殊单位是什么？"
        })
    )
    q2 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "内容"
        })
    )
    q3 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "内容"
        })
    )
    q4 = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "内容"
        })
    )