from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from .models.products import Product
from .models.variations import Variation, VariationCategoryChoice


class StoreListView(ListView):
    model = Product
    template_name = "store/list.html"
    context_object_name = "products"
    queryset = Product.objects.filter(is_available=True)


store_list_view = StoreListView.as_view()


class ProductDetailView(DetailView):
    model = Product
    template_name = "store/detail.html"
    context_object_name = "product"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    # override get_context_data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context["size_variations"] = Variation.objects.filter(
            product=product, variation_category=VariationCategoryChoice.SIZE
        )
        context["color_variations"] = Variation.objects.filter(
            product=product, variation_category=VariationCategoryChoice.COLOR
        )
        return context


product_detail_view = ProductDetailView.as_view()
