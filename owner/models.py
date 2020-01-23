from django.db import models
from Account.models import Account

# Create your models here.
class OwnerInfo(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Room(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='media/image')
    type = models.CharField(max_length=100,)
    location = models.CharField(max_length=100)
    user = models.ForeignKey(OwnerInfo, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.name
