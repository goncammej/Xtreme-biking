# Generated by Django 4.2.7 on 2023-11-28 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_customer_alter_shippingaddress_customer'),
        ('client', '0002_customer_delete_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]