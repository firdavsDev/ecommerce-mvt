from django import forms

from ..models.accounts import CustomUser


# form for user password reset
class ResetPasswordForm(forms.Form):
    email = forms.EmailField(label="Email")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is not registered!")
        return email


class ConfirmPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password"
    )

    # v2 is using validation
    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return confirm_password
