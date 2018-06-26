from django import forms

class SandboxSignupForm(forms.Form):
    email = forms.EmailField(label="Email")