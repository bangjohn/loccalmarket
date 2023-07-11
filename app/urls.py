from django.urls import path

from app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("product-list/", views.product_list, name="product_list"),
    path("add-product/", views.add_product, name="add_product"),
    path("temp-image-upload/", views.temp_image_upload, name="temp_image_upload"),
    path("temp-image-delete/", views.temp_image_delete, name="temp_image_delete"),
]
