from django.db import models

# Create your models here.
class createUser(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    date = models.DateField()
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    
    def __str__(self):
        return self.name