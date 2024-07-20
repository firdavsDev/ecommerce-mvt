"""
Send reset password email to the user.
"""

from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from accounts.utils import get_activation_link
from common.background_job import run_in_background


@run_in_background
def send_reset_password_email(user, request):
    """Sends a reset password email to the user.

    Args:
        user (User): The user.
        request (HttpRequest): The request object.
    """
    try:
        subject = "Reset your password"
        message = render_to_string(
            "accounts/reset_password.html",
            {
                "full_name": user.get_full_name,
                "reset_password_link": get_activation_link(user, request),
            },
        )
        email = EmailMessage(subject, message, to=[user.email])
        email.send()
    except Exception as e:
        raise e
