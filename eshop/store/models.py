from django.db import models

# Create your models here.
# """ Products
# - Nom
# - Prix
# - Description
# - Qte en stock
# - Image
# - recommandations
# """

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products", blank=True, null=True)
    slug = models.SlugField(max_length=128)

    def __str__(self):
        return f"{self.name} (stock = {self.stock})"