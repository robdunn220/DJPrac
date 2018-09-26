from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "id": "form_full_name", "placeholder": "Full Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "id": "form_email", "placeholder": "Email"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Your Message"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email must be @gmail.com")
        return email

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
