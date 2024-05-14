from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.description}"


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon')
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2024, validators=[
        MinValueValidator(2015),
        MaxValueValidator(2024)
    ])

    def __str__(self):
        return f"{self.name} ({self.year}) {self.type}"
