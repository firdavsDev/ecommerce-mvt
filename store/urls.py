from django.urls import path

from .views import product_detail_view, store_list_view

app_name = "store"

urlpatterns = [
    path("", store_list_view, name="store_list"),
    path("<slug:slug>/", product_detail_view, name="product_detail"),
]
