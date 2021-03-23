from django.db import models

# Create your models here.
class organization(models.Model):

    username = models.CharField(max_length=1000)
    email= models.EmailField()
    # img= models.ImageField( upload_to='pics')
    number = models.CharField(max_length=10)
    password= models.CharField(max_length=200)
    des = models.TextField()