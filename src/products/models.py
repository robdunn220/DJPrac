from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=7, default=0.00)
    image = models.FileField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.title
