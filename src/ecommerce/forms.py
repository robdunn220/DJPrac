from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

# Class creation of the contact form
class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id": "form_full_name", "placeholder": "Full Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "id": "form_email", "placeholder": "Email"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Your Message"}))

    # Method to validate email is a Gmail address
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email must be @gmail.com")
        return email

# Class creation of the login form (Need to add validation for nonexisting account, and a reroute to registations)
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

# Class creation of the registration form
class RegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

    # Method to check for existing username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username taken')
        return username

    # Method to check for existing email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email taken')
        return email

    # Method to check for matching passwords
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError('Passwords must match')
        return data
