from django.db import models
import random
import os

# Create your models here.
def get_file_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1,100)
    name, ext = get_file_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f"products/{final_filename}"

class ProductManager(models.Manager):
    def featured(self):
        return self.get_queryset().filter(featured=True)
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

class Product(models.Model):
    title = models.CharField(max_length=120)
    # upload_image_path = f'products/{title}'
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=7, default=0.00)
    image = models.ImageField(upload_to=upload_image_path , null=True, blank=True)
    featured = models.BooleanField(default=False)

    objects = ProductManager()

    def __str__(self):
        return self.title
