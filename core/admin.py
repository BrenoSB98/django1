from django.contrib import admin

from .models import Client, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
