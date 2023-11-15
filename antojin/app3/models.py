from django.db import models

# Create your models here.


class Dress(models.Model):
    title = models.CharField(max_length=300)
    size = models.CharField(max_length=250)
    description=models.TextField(default=True,blank=True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=5)
    image_url = models.CharField(max_length=10000,blank=True,null=True)
    dress_available = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.title
