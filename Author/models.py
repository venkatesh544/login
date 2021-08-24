from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


