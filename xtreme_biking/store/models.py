from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    image_url = models.CharField(max_length=100, null=False, blank=False)
    availability = models.IntegerField(null=False, validators=[MinValueValidator(0)])

    class Category(models.TextChoices):
        MOUNTAIN_BIKE = 'Bicleta de montaña'
        URBAN_BIKE = 'Bicicleta urbana'
        ROAD_BIKE = 'Bicicleta de carretera'
        SUSTITUTION = 'Pieza de sustitución'
    
    category = models.CharField(max_length=30, choices=Category.choices, default=Category.MOUNTAIN_BIKE)

    def __str__(self):
        return self.title

    


