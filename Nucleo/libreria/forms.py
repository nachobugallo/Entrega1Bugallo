from django import forms

class Formulario_Books(forms.Form):
    name = forms.CharField(max_length=50)
    price = forms.FloatField()
    author = forms.CharField(max_length=200)
    is_active = forms.BooleanField()
    book_is_atp = forms.BooleanField()
    book_category = forms.CharField(max_length=50)
    stock = forms.IntegerField()