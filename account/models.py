from django.db import models
import datetime
# Create your models here.

# Create your models here.
class ash(models.Model):
    firstname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    def __str__(self):
        return self.username



