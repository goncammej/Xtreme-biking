from django.db import models
from accounts.models import CustomUser
from django.utils.translation import gettext_lazy as _


class Customer(models.Model):
    user = models.OneToOneField(
        CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=254, null=True)
    email = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class CustomerShipping(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)
    address = models.CharField(
        _("Dirección"), max_length=200)
    city = models.CharField(_("Ciudad"), max_length=200)
    state = models.CharField(
        _("Localidad"), max_length=200)
    zipcode = models.CharField(
        _("Código postal"), max_length=200)
    predetermined = models.BooleanField(default=False)

    def __str__(self):
        return self.address


class CustomerPaymentMethod(models.Model):
    class PaymentMethod(models.TextChoices):
        COD = 'Contra reembolso', _('Contra reembolso')
        CARD = 'Pago online', _('Pago online')

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)
    method = models.CharField(_("Método de pago"), max_length=30,
                              choices=PaymentMethod.choices, default=PaymentMethod.COD)
