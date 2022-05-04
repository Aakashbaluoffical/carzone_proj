
# Create your models here.
from django.db import models


class contactus(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    number = models.IntegerField()
    message = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.fullname
