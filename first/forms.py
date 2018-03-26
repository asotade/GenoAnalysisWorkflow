from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','placeholder': "Entrer votre nom d'utilisatuer"}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','type':'password','placeholder':'Entrer votre mot de passe'}))
