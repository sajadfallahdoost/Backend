from django.contrib import admin

from shop.models import Product, ProductImage, Comment

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Comment)
