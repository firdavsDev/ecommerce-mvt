from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import redirect
from django.utils.http import urlsafe_base64_decode
from django.views import View

from accounts.models.accounts import CustomUser


class ActivateEmailView(View):
    """
    - This view is used to activate the user's account.
    """

    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, "Account activated successfully!")
            return redirect("accounts:login")
        else:
            messages.error(request, "Activation link is invalid!")
            return redirect("store:store_list")


activate_email = ActivateEmailView.as_view()
