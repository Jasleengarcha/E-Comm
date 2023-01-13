from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SignUp(models.Model):
    try:
        first_name = models.CharField(max_length=15)
        last_name = models.CharField(max_length=15)
        email = models.EmailField(unique=True)
        phone = models.CharField(max_length=13)
        address = models.CharField(max_length=60)
    except Exception:
        print("Email is already registed")

    def __str__(self):
        return self.first_name

class AddProduct(models.Model):
    product_img = models.ImageField()
    product_id = models.CharField(max_length=15)
    product_name = models.CharField(max_length=50)
    product_price = models.CharField(max_length=20)
    product_desc = models.CharField(max_length=150)

    def __str__(self):
        return self.product_id