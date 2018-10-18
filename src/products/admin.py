from django.contrib import admin
from import_export import resources

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = Product

admin.site.register(Product)
