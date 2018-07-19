from django.contrib import admin

from products.models import Product, Category, Media

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Media)
