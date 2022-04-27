from django.db import models
from eshop.settings import AUTH_USER_MODEL

# Product Model.
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

# Order Model.
# """ Order(Transaction)
# - Utilisateur
# - Produit
# - Qte en stock
# - Commandé ou non
# """

class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} (quantiy = {self.quantity})"

# Cart Model.
# """ Cart(Pannier)
# - Utilisateur
# - Produits
# - Date commande
# """
class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username
