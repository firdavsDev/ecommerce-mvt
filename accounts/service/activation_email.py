from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from accounts.utils import get_activation_link
from common.background_job import run_in_background


@run_in_background
def send_activation_email(user, request):
    """Sends an activation email to the user.

    Args:
        user (User): The user.
        request (HttpRequest): The request object.
    """
    try:
        subject = "Activate your account"
        message = render_to_string(
            "accounts/activation.html",
            {
                "full_name": user.get_full_name,
                "activation_link": get_activation_link(user, request),
            },
        )
        email = EmailMessage(subject, message, to=[user.email])
        email.send()
    except Exception as e:
        raise e
