# Generated by Django 4.2.7 on 2023-12-02 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_customershipping_customerpaymentmethod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerpaymentmethod',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.customer'),
        ),
        migrations.AlterField(
            model_name='customerpaymentmethod',
            name='method',
            field=models.CharField(blank=True, choices=[('Contra reembolso', 'Cod'), ('Pago online', 'Card')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customershipping',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customershipping',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customershipping',
            name='customer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='client.customer'),
        ),
        migrations.AlterField(
            model_name='customershipping',
            name='state',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customershipping',
            name='zipcode',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
