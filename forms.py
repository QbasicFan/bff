from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from .models import bookMark, defi, defiCard

class bookMarkForm(forms.ModelForm):
    class Meta:
        model = bookMark
        fields = ['title','link','cate','rate']




class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2']
    def save(self , commit=True):
        user = super(RegistrationForm , self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class UserForm (forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','password']




class defiForm(forms.ModelForm):
    class Meta:
        model = defi
        fields = ['title']



class defiCardForm(forms.ModelForm):
    class Meta:
        model = defiCard
        fields = ['title','mr','en','fr','sp']


