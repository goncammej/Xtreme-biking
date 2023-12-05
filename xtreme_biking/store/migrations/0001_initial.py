# Generated by Django 4.2.7 on 2023-12-04 23:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('image_url', models.CharField(max_length=100)),
                ('availability', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('category', models.CharField(choices=[('Bicleta de montaña', 'Mountain Bike'), ('Bicicleta urbana', 'Urban Bike'), ('Bicicleta de carretera', 'Road Bike'), ('Pieza de sustitución', 'Sustitution')], default='Bicleta de montaña', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)])),
                ('comment', models.TextField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
