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


class RegionAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = [
        "name",
    ]
    list_per_page = 10


admin.site.register(Region, RegionAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = ["name", "region"]
    search_fields = [
        "name",
    ]
    list_per_page = 10
    list_filter = ["region"]


admin.site.register(District, DistrictAdmin)
