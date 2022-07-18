from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TheUser, Product, Cart

admin.site.register(TheUser, UserAdmin)
admin.site.register(Product)
admin.site.register(Cart)
