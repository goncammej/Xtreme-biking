from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from client.models import Customer, CustomerPaymentMethod, CustomerShipping


@receiver(post_save, sender=CustomerShipping)
def create_address(sender, instance, created, **kwargs):
    if created:
        predetermined_shipping = CustomerShipping.objects.filter(
            customer=instance.customer, predetermined=True)
        if not predetermined_shipping:
            instance.predetermined = True
            instance.save()
