from django import forms
from .models import *
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth.models import User
from .models import UserDetail


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserDetail
        fields = ["username", "email", "password1", "password2", "phone_no", "address"]


class ProductDetailForm(forms.Form):
    product_name = forms.CharField(
        max_length=250,
        label="Product Name",
    )
    brand = forms.CharField(
        max_length=200,
        label="Brand Name",
    )
    price = forms.CharField(
        max_length=200,
        label="Price",
    )
    description = forms.CharField(label="Description", widget=forms.Textarea)
    stock = forms.IntegerField(
        label="Stock",
    )


class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ["phone_no", "address"]


# class OrderDetailForm(forms.ModelForm):
#     class Meta:
#         model = OrderDetail
#         fields = ["user", "product", "order_detail", "delivery_date", "address"]


class OrderDetailForm(forms.Form):
    user = forms.ModelChoiceField(queryset=UserDetail.objects.all())
    product = forms.ModelChoiceField(queryset=ProductDetail.objects.all())
    quantity = forms.IntegerField()
    order_date = forms.DateTimeField(initial=timezone.now)
    delivery_date = forms.DateTimeField(required=False)
    address = forms.CharField(max_length=150, required=False)


class CartDetailForm(forms.ModelForm):
    class Meta:
        model = CartDetail
        fields = ["user", "product", "quantity"]
