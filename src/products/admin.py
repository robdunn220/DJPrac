from django.contrib import admin
from import_export import resources

# Register your models here.
from .models import Product

admin.site.register(Product)
