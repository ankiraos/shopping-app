from django.contrib import admin
from .models import ProductDetail, UserDetail, CartDetail, OrderDetail
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(ProductDetail)


@admin.register(UserDetail)
class UserDetailAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "phone_no",
        "address",
        "is_staff",
        "is_active",
    )
    list_filter = ("is_staff", "is_active")
    search_fields = ("username", "email", "phone_no", "address")

    # Adding custom fields to fieldsets
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("phone_no", "address")}),)

    # To include custom fields in add form
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("phone_no", "address")}),
    )


@admin.register(CartDetail)
class CartDetailAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "quantity"]


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "product",
        "order_date",
        "delivery_date",
        "address",
    ]
