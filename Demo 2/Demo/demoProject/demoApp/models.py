from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    number=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    symptoms=models.CharField(max_length=200)
    severity=models.CharField(max_length=20)
    option=models.CharField(max_length=200)
    date=models.CharField(max_length=15)
    def __str__(self):
        return self.name
