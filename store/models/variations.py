from django.db import models

from ..managers.variations import VariationCategoryChoice, VariationManager
from .products import BaseModel, Product


class Variation(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="variations"
    )
    variation_category = models.CharField(
        max_length=100, choices=VariationCategoryChoice.choices
    )
    variation_value = models.CharField(max_length=100)

    # custom manager
    objects = VariationManager()

    def __str__(self):
        return self.variation_value

    class Meta:
        verbose_name_plural = "Variations"
        verbose_name = "Variation"
