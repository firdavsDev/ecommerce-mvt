from django.db import models
from django.utils.text import slugify

from common.file_path_renamer import PathAndRename
from common.models import BaseModel

product_thumbnail_path_and_rename = PathAndRename("products/thumbnails")
products_images_path_and_rename = PathAndRename("products/images")


class ProductCategory(BaseModel):
    name = models.CharField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"


class Product(BaseModel):
    name = models.CharField(max_length=255, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, related_name="products"
    )
    is_available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=0)
    thumbnail = models.ImageField(
        upload_to=product_thumbnail_path_and_rename, blank=True, null=True
    )

    @property
    def is_in_stock(self):
        return self.stock > 0

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Products"
        verbose_name = "Product"


class ProductImage(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to=products_images_path_and_rename)

    def __str__(self):
        return f"{self.product.name} image"

    class Meta:
        verbose_name_plural = "Product Images"
        verbose_name = "Product Image"
