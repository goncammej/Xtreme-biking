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

    
class Rating(models.Model):
    bike = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, validators=[MaxValueValidator(5)])
    comment = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, default='')
    email = models.EmailField()

