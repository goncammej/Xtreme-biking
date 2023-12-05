from django.db.models.signals import post_save, pre_delete
from .models import CustomUser
from django.dispatch import receiver
from client.models import Customer, CustomerPaymentMethod, CustomerShipping


@receiver(post_save, sender=CustomUser)
def create_user(sender, instance, created, **kwargs):
    if created:
        customer = Customer.objects.create(user=instance)
        customer.name = instance.name
        customer.email = instance.email
        customer.save()

        payment_method = CustomerPaymentMethod.objects.create(
            customer=customer)
        payment_method.save()
