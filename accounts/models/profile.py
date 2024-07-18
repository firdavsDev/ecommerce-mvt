from django.db import models

from common.file_path_renamer import PathAndRename
from common.models import BaseModel, District, Region

from .accounts import CustomUser

user_avatar_path = PathAndRename("avatars/")


class Profile(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=user_avatar_path, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} Profile"

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
