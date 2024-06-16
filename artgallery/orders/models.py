from django.db import models
from django.contrib.auth.models import User
from galleryItems.models import GalleryItems
# Create your models here.


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    class Meta:
        db_table = 'cart'

    def __str__(self):
        return f"Cart of {self.user.username}"



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(GalleryItems, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'cartitem'

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"