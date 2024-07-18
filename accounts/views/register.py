from django.views.generic import CreateView

from ..forms import CustomUserCreationForm
from ..models.accounts import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "accounts/register.html"
    success_url = "/"


register = RegisterView.as_view()
