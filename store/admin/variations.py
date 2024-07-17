from django.contrib import admin

from ..models.variations import Variation


class VariationAdmin(admin.ModelAdmin):
    list_display = ("product", "variation_category", "variation_value", "is_active")
    list_filter = ("product", "variation_category", "is_active")
    search_fields = ("product__name",)
    list_editable = ("is_active",)
    autocomplete_fields = ("product",)


admin.site.register(Variation, VariationAdmin)
