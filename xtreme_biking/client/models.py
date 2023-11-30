from django.db import models
from accounts.models import CustomUser

class Customer(models.Model):
	user = models.OneToOneField(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=254, null=True)
	email = models.CharField(max_length=254)

	def __str__(self):
		return self.name

class CustomerShipping(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
	address = models.CharField(max_length=200, null=True)
	city = models.CharField(max_length=200, null=True)
	state = models.CharField(max_length=200, null=True)
	zipcode = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.address

class CustomerPaymentMethod(models.Model):
	class PaymentMethod(models.TextChoices):
		COD = 'Contra reembolso'
		CARD = 'Pago online'
  
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
	method = models.CharField(max_length=30, choices=PaymentMethod.choices, null=True)