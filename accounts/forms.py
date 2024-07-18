from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models.accounts import CustomUser


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ["password1", "password2"]:
            self.fields[fieldname].help_text = None

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name"]
        labels = {
            "email": "Email",
            "first_name": "Enter your first name",
            "last_name": "Enter your last name",
        }


# form for user login
class CustomUserLoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    def __init__(self, request, *args, **kwargs):
        # simply do not pass 'request' to the parent
        super().__init__(*args, **kwargs)
