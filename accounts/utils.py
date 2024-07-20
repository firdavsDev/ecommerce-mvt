# domain.uz/url/uid64/token(change password)

from asyncio.log import logger

from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def get_activation_link(user, request) -> str:
    """Generates an activation link for the user.

    Args:
        user (int): The user's ID.
        request (HttpRequest): The request object.

    Returns:
        str: The activation link.
    """
    try:
        domain = get_current_site(request)
        uid64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        return f"http://{domain}/accounts/activate/{uid64}/{token}"
    except Exception as e:
        logger.error(e)
        raise e
