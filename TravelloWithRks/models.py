from django.db import models

# Create your models here.

class Destination(models.Model):
    # id : int
    # name : str
    name = models.CharField(max_length=100)
    # img : str
    img = models.ImageField(upload_to='pics')
    # desc : str
    desc = models.TextField()
    # price : int
    price = models.IntegerField()
    # offer: bool
    offer = models.BooleanField(default=False)
