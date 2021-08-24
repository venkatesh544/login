from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.
class BDAdata(models.Model):
    userid = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.userid


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',max_length=80, unique=True)  # Mandatory
    username = models.CharField( max_length=30, blank=True, null=True)
    # General
    # Area
    state = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    # Contact
    phone = models.CharField(max_length=13, null=True,blank=True)
    password = models.CharField(max_length=16)

    USERNAME_FIELD ='email'

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs')

    def __str__(self):
        return self.title

    def delete(self,*args,**kwargs):
        self.pdf.delete()
        super().delete(*args,**kwargs)