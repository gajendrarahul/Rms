from django.db import models
from Account.models import Account

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    no_of_person = models.CharField(max_length=50, default=0, null=True, blank=True)
    user = models.OneToOneField(Account, on_delete=models.CASCADE,default=None)
    def __str__(self):
        return self.name
