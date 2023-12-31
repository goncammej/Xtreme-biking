# Generated by Django 4.2.7 on 2023-12-04 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, null=True)),
                ('email', models.CharField(max_length=254)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerShipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, verbose_name='Dirección')),
                ('city', models.CharField(max_length=200, verbose_name='Ciudad')),
                ('state', models.CharField(max_length=200, verbose_name='Localidad')),
                ('zipcode', models.CharField(max_length=200, verbose_name='Código postal')),
                ('predetermined', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.customer')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerPaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('Contra reembolso', 'Cod'), ('Pago online', 'Card')], default='Contra reembolso', max_length=30, verbose_name='Método de pago')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.customer')),
            ],
        ),
    ]
