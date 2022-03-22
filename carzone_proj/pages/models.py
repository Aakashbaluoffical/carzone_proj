from django.db import models

# Create your models here.

class team(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    position = models.CharField(max_length=256)
    photos = models.ImageField(upload_to='photos/%y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    google_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


