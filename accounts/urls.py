from django.urls import path

from .views.activate import activate_email
from .views.login import login_view
from .views.logout import logout_view
from .views.register import register

app_name = "accounts"

urlpatterns = [
    # Auth
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("activate/<uidb64>/<token>/", activate_email, name="activate_email"),
]
