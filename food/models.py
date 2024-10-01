from django.db import models

class Item(models.Model):
    def __str__(self):
        return self.name
        
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=500)
    image = models.CharField(max_length=500 , default="https://img.freepik.com/premium-vector/restaurant-logo-design_1128391-17280.jpg")
