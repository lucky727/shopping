from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="products/")
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    def __str__(self):
        return self.name