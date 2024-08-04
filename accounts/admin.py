from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models.accounts import CustomUser
from .models.profile import Profile


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["email", "first_name", "last_name", "is_active", "is_staff"]
    list_filter = ["is_active", "is_staff"]
    search_fields = ["email", "first_name", "last_name"]
    ordering = ["email"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "first_name", "password1", "password2"),
            },
        ),
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Important dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "avatar",
        "bio",
        "birth_date",
        "region",
        "district",
        "address",
    ]
    list_filter = ["region", "district"]
    search_fields = ["user__first_name"]
    autocomplete_fields = ["user", "region", "district"]


admin.site.register(Profile, ProfileAdmin)
