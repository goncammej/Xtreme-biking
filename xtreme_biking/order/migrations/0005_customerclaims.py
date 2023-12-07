# Generated by Django 4.1 on 2023-12-07 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_customerreviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerClaims',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim', models.TextField(verbose_name='Reclamación')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
        ),
    ]
