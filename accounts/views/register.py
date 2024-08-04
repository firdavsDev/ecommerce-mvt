from django.shortcuts import redirect
from django.views.generic import CreateView

from ..forms.user_forms import CustomUserCreationForm
from ..models.accounts import CustomUser
from ..service.activation_email import send_activation_email


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "accounts/register.html"
    success_url = "/"

    def form_valid(self, form):
        response = super().form_valid(form)
        # Send activation email function call
        send_activation_email(self.object, self.request)
        return response

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("store:store_list")
        return super().get(request, *args, **kwargs)


register = RegisterView.as_view()
