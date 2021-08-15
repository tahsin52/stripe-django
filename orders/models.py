from django.db import models
from django.conf import settings

from store.models import Product


class Orders(models.Model):
    user           = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_user')
    full_name      = models.CharField(max_length=155)
    address1       = models.CharField(max_length=155)
    address2       = models.CharField(max_length=155)
    city           = models.CharField(max_length=155)
    phone          = models.CharField(max_length=155)
    post_code      = models.CharField(max_length=155)

    created        = models.DateTimeField(auto_now_add=True)
    updated        = models.DateTimeField(auto_now=True)

    total_paid     = models.DecimalField(max_digits=5, decimal_places=2)
    order_key      = models.CharField(max_length=155)
    billing_status = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.full_name



class OrderItem(models.Model):
    order    = models.ForeignKey(Orders,
                                 related_name='items',
                                 on_delete=models.CASCADE)

    product   = models.ForeignKey(Product,
                                  related_name='order_item',
                                  on_delete=models.CASCADE)

    price      = models.DecimalField(max_digits=5, decimal_places=2)
    quantity   = models.PositiveIntegerField(default=1)


    def __str__(self):
        return str(self.id)