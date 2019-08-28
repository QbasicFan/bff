from django import forms
from .models import bookMark

class bookMarkForm(forms.ModelForm):
    class Meta:
        model = bookMark
        fields = ['title','link','cate','rate']
