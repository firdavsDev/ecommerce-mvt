from django.urls import path

from .views.login import login_view
from .views.logout import logout_view
from .views.register import register

app_name = "accounts"

urlpatterns = [
    # Auth
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
