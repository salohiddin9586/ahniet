from django.contrib import admin

from django.contrib import admin
from apps.products.models import Product, ProductImage


# class ProductImageLine(admin.ModelAdmin):
#     model = Product.get_images().through
#     extra = 1


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['image']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['category']
    search_fields = ['title']