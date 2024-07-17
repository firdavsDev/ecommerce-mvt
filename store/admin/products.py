from django.contrib import admin
from django.utils.html import format_html

from ..models.products import Product, ProductCategory, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 5


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "thumbnail",
        "name",
        "price",
        "category",
        "is_available",
        "stock",
        "created_at",
        "is_active",
    )
    list_filter = ("category", "is_available", "is_active")
    search_fields = ("name", "category__name")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("price", "is_available", "stock", "is_active")
    inlines = [ProductImageInline]
    autocomplete_fields = ("category",)

    def thumbnail(self, obj):
        return format_html(f'<img src="{obj.thumbnail.url}" width="50" height="50" />')

    thumbnail.short_description = "Thumbnail"


admin.site.register(Product, ProductAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)
    list_editable = ("is_active",)


admin.site.register(ProductCategory, ProductCategoryAdmin)
