from django.db import models
from django.core.validators import MaxValueValidator
from django.db import models
from django.core.validators import MaxValueValidator

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.CharField(max_length=100)
    availability = models.IntegerField(default=0)
    #cart = models.ForeignKey(Cart, on_delete=models.CASCADE) Many to one hacia carrito

    class Category(models.TextChoices):
        MOUNTAIN_BIKE = 'Bicicleta de montaña'
        URBAN_BIKE = 'Bicicleta urbana'
        ROAD_BIKE = 'Bicicleta de carretera'
        ACCESSORY = 'Accesorio'
    
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

