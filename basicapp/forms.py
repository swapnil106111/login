from django import forms

class loginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class signupForm(forms.Form):
	email = forms.EmailField(required=True)
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)
	extra_email = forms.EmailField(required=False)