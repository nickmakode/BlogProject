from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    weight=models.FloatField()
    price=models.FloatField()
    image=models.ImageField(upload_to="images/products",null=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)


