from django.db import models

from django.utils.translation import gettext_lazy as _

from store.models import Product
from client.models import Customer
from django.core.validators import MaxValueValidator, MinValueValidator


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    total = models.FloatField(validators=[MinValueValidator(0.0)], null=True)

    class Status(models.TextChoices):
        SENT = 'Enviado'
        DELIVERED = 'Entregado'

    status = models.CharField(
        max_length=30, choices=Status.choices, default=Status.SENT)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = True
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        if total > 1000:
            shipping = False
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def has_review(self):
        review = CustomerReviews.objects.get(order=self)
        if review:
            return True
        else:
            return False
        
    @property
    def has_claim(self):
        claim = CustomerClaims.objects.get(order=self)
        if claim:
            return True
        else:
            return False



class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

class CustomerReviews(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    review = models.TextField(_("Valoración"), null=False)

    def __str__(self):
        return self.review
    
class CustomerClaims(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    claim = models.TextField(_("Reclamación"), null=False)
    class StatusClaim(models.TextChoices):
        OPEN = 'Abierto'
        CLOSED = 'Cerrado'

    status = models.CharField(
        max_length=30, choices=StatusClaim.choices, default=StatusClaim.OPEN)

    def __str__(self):
        return self.claim
