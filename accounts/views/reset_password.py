from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import redirect, render
from django.utils.http import urlsafe_base64_decode
from django.views import View

from accounts.forms.reset_password import ConfirmPasswordForm, ResetPasswordForm
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


reset_password = ResetPasswordView.as_view()


class ActivateResetPasswordEmailView(View):
    """
    - This view is used to activate the user's account.
    """

    form = ConfirmPasswordForm

    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            # set the user id in the session
            request.session["uid"] = uid
            messages.success(request, "Please enter your new password.")
            return render(
                request,
                "accounts/reset_password_confirm.html",
                context={"form": self.form},
            )
        else:
            messages.error(request, "Reset password link is invalid!")
            return redirect("accounts:login")

    def post(self, request, uidb64, token):
        try:
            uid = request.session.get("uid")
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            form = self.form(request.POST)
            if form.is_valid():
                password = form.cleaned_data.get("password")
                user.set_password(password)
                user.save()
                messages.success(request, "Password reset successfully!")
                return redirect("accounts:login")
            return render(
                request, "accounts/reset_password_confirm.html", {"form": form}
            )
        else:
            messages.error(request, "Reset password link is invalid!")
            return redirect("accounts:login")


activate_reset_pass_email = ActivateResetPasswordEmailView.as_view()
