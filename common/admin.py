from django.contrib import admin
from django.contrib.auth.models import Group

from .models import District, Region

# unregister the Group model from the admin
admin.site.unregister(Group)
admin.site.site_header = "eCommerce Admin"
admin.site.site_title = "eCommerce Admin Portal"
admin.site.index_title = "Welcome to eCommerce Admin Portal"
admin.site.empty_value_display = "Mavjud emas"

# Register your models here.
admin.site.register(Region)
admin.site.register(District)
