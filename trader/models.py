from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class ItemType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    item_type = models.ForeignKey(ItemType,on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published")
