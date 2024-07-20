from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from accounts.forms import ResetPasswordForm
from accounts.models.accounts import CustomUser
from accounts.service.reset_password_email import send_reset_password_email


class ResetPasswordView(View):
    """
    - This view is used to reset the user's password.
    """

    def get(self, request):
        form = ResetPasswordForm()
        return render(request, "accounts/reset_password.html", {"form": form})

    def post(self, request):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            user = CustomUser.objects.get(email=email)
            # call the function to send the password reset email
            send_reset_password_email(user, request)
            messages.success(request, "Password reset email sent successfully!")
            return redirect("accounts:login")
        return render(request, "accounts/reset_password.html", {"form": form})
