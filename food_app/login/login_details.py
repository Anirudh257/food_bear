from django import forms

class user_login_details(forms.Form):
	username = forms.CharField(label = '', required = True, max_length = 30, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password = forms.CharField(label = '', required = True, max_length = 30, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))