from django.contrib import admin
from .models import Product, Offer

# Register your models here.
# These models will be visible in the admin panel


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    # These are the keys with values we want to show
    # in the admin panel under the Products category
    # (it is the list of products)


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')
    # These are the keys with values we want to show
    # in the admin panel under the Products category
    # (it is the list of products)


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
