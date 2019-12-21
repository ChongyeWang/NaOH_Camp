from django import forms
from .models import Product


class ProductForm(forms.Form):
    name = forms.CharField(
    	max_length=30,
    	widget=forms.TextInput(
            attrs={
                'style': 'border-color: black;',
                'placeholder': '商品名称'
            }
        ))
        
    description = forms.CharField(
    	max_length=200,
    	widget=forms.TextInput(
            attrs={
                'style': 'border-color: black;',
                'placeholder': '请填写联系方式，以便买家直接和您沟通。',
                'class': 'form-control'
            }
        ))


    image = forms.ImageField() 

    CHOICES= (
        (1, 'vehicles'),
        (2, 'production'),
        (2, 'Other'),
    )

    select = forms.CharField(widget=forms.Select(choices=CHOICES))

    price = forms.IntegerField()

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', )
    