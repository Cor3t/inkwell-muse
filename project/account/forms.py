from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

