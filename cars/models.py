from django.db import models
from brands.models import Brand
from django.contrib.auth.models import User

class Car(models.Model):
    car_title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.CharField(max_length=12)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)
    purchased_by = models.ManyToManyField(User, related_name='purchased_cars', blank=True)
    images = models.ImageField(upload_to='cars/media/uploads/')
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.car_title 
    
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    Comments = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"Comments by {self.name}"