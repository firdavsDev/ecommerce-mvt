from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView as AuthLoginView
from django.shortcuts import redirect

from ..forms.user_forms import CustomUserLoginForm
from ..models.accounts import CustomUser


class LoginView(AuthLoginView):
    template_name = "accounts/login.html"
    form_class = CustomUserLoginForm
    model = CustomUser

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(email=email, password=password)
        if user is not None:
            messages.success(self.request, "You have successfully logged in.")
            login(self.request, user)
            return redirect("accounts:profile")
        messages.error(self.request, "Invalid email or password.")
        return super().form_invalid(form)


login_view = LoginView.as_view()
