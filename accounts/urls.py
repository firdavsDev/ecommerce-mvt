from django.urls import path

from .views.activate import activate_email
from .views.login import login_view
from .views.logout import logout_view
from .views.profile import profile_view
from .views.register import register
from .views.reset_password import activate_reset_pass_email, reset_password

app_name = "accounts"

urlpatterns = [
    # Auth
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("activate/<uidb64>/<token>/", activate_email, name="activate_email"),
    # Reset password
    path("reset_password/", reset_password, name="reset_password"),
    path(
        "reset_password/<uidb64>/<token>/",
        activate_reset_pass_email,
        name="activate_reset_pass_email",
    ),
    # Profile
    path("profile/", profile_view, name="profile"),
]
