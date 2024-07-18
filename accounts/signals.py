"""
Create singals for the accounts app

"""

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models.accounts import CustomUser
from .models.profile import Profile


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
