from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.


class ProductDetail(models.Model):
    product_name = models.CharField(max_length=70)
    brand = models.CharField(max_length=20)
    price = models.CharField(max_length=10)
    description = models.TextField()
    stock = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.product_name


class UserDetail(AbstractUser):
    phone_no = models.IntegerField(null=True)
    address = models.CharField(max_length=150)


class CartDetail(models.Model):
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    quantity = models.IntegerField()


# card_detail.product.brand

# brand=forms.methodField(read_only=True)

# def get_branch(self):
#     return self.pro


class OrderDetail(models.Model):
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True)
    address = models.CharField(max_length=150, null=True)
