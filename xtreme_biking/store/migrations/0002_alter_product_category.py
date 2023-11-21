# Generated by Django 4.2.5 on 2023-11-20 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Bicleta de montaña', 'Mountain Bike'), ('Bicicleta urbana', 'Urban Bike'), ('Bicicleta de carretera', 'Road Bike'), ('Accesorio', 'Accessory')], default='Bicleta de montaña', max_length=30),
        ),
    ]