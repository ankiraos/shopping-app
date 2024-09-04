from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .models import ProductDetail, UserDetail, CartDetail, OrderDetail
from .forms import ProductDetailForm, OrderDetailForm, CartDetailForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.utils import timezone


# Create your views here.
def home(request):
    products = ProductDetail.objects.all()
    # if products:
    #     return redirect("home")
    return render(request, "home.html", context={"products": products})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            messages.error(request, "There was an error with your registration.")
    else:
        form = RegisterForm()
    return render(request, "register.html", context={"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                messages.success(request, "Login successful")
                return redirect("home")
            else:
                messages.success(request, "Login successful")
                return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")


@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    return render(request, "logout.html")


@login_required
def user_list(request):
    user = request.user
    users = UserDetail.objects.filter(username=user)
    return render(request, "user_list.html", {"users": users})


def delete_user(request):
    user = request.user
    if user:
        user = UserDetail.objects.get(username=user)
        user.delete()
        return redirect("register")


# add_product , del_product , product_list
@login_required
def add_productview(request):
    if request.method == "POST":
        form = ProductDetailForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data.get("product_name")
            brand = form.cleaned_data.get("brand")
            price = form.cleaned_data.get("price")
            description = form.cleaned_data.get("description")
            stock = form.cleaned_data.get("stock")
            ProductDetail.objects.create(
                product_name=product_name,
                brand=brand,
                price=price,
                description=description,
                stock=stock,
            )
            return redirect("product_list")
    else:
        form = ProductDetailForm()
        return render(request, "add_product.html", context={"form": form})


@login_required
def del_product(request, id=id):
    # if request.method == "POST":
    print(id)
    # product = get_object_or_404(CartDetail, id=id)
    product = ProductDetail.objects.filter(id=id)
    print(product)
    product.delete()
    return redirect("product_list")


@login_required
def product_list(request):
    products = ProductDetail.objects.all()
    return render(request, "product_list.html", {"products": products})


# order_detail , del order, order list
@login_required
def orderdetail_view(request):
    if request.method == "POST":
        form = OrderDetailForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("user")
            product = form.cleaned_data.get("product")
            brand = form.cleaned_data.get("brand")
            quantity = form.cleaned_data.get("quantity")
            order_date = form.cleaned_data.get("order_date")
            delivery_date = form.cleaned_data.get("delivery_date")
            address = form.cleaned_data.get("address")

            OrderDetail.objects.create(
                user=user,
                product=product,
                brand=brand,
                quantity=quantity,
                order_date=order_date,
                delivery_date=delivery_date,
                address=address,
            )
            return redirect("order_list")
    else:
        form = OrderDetailForm()
    return render(request, "order_detail.html", context={"form": form})


def add_order(request, id=id):
    user = request.user
    product = ProductDetail.objects.get(id=id)
    quantity = 1
    order_date = timezone.now()
    address = request.user.address
    OrderDetail.objects.create(
        user=user,
        product=product,
        quantity=quantity,
        order_date=order_date,
        address=address,
    )
    return redirect("order_list")


@login_required
def del_order(request, id=id):
    product = get_object_or_404(OrderDetail, id=id)
    product.delete()
    return redirect("order_list")


@login_required
def users_of_order_list(request):
    user = request.user
    if user.is_staff:
        users_with_orders = CartDetail.objects.values_list(
            "user_id", flat=True
        ).distinct()
        users = UserDetail.objects.filter(id__in=users_with_orders)
        has_orders = users.exists()
        return render(
            request,
            "users_of_order_list.html",
            {"users": users, "has_orders": has_orders},
        )


@login_required
def order_list(request):
    user = request.user
    if request.user.is_staff:
        orders = OrderDetail.objects.all()
        return render(request, "order_list.html", {"orders": orders})
    else:
        orders = OrderDetail.objects.filter(user=user)
        return render(request, "order_list.html", {"orders": orders})


@login_required
def orders_list(request, user_id):
    user = get_object_or_404(UserDetail, id=user_id)
    orders = OrderDetail.objects.filter(user=user)
    return render(request, "order_list.html", {"orders": orders})


# addcart, delcart, cartlist
@login_required
def addcart_view(request, id=id):
    user = request.user
    print(user, "!")
    if request.method == "POST":
        form = CartDetailForm(request.POST)
        if form.is_valid():
            user = user
            product = form.cleaned_data.get("product.id")
            quantity = form.cleaned_data.get("quantity")
            print(user)
            CartDetail.objects.create(user=user, product=product, quantity=quantity)
            return redirect("cart_list")
    else:
        form = CartDetailForm()
        return render(request, "addcart.html", context={"form": form})


def addcart_by_plist(request, id=id):
    product = ProductDetail.objects.get(id=id)
    print(product)
    user = request.user
    print(user)
    quantity = 1
    CartDetail.objects.create(user=user, product=product, quantity=quantity)
    return redirect("cart_list")


@login_required
def del_addcart(request, id=id):
    if request.method == "POST":
        product = CartDetail.objects.filter(id=id)
        product.delete()
        return redirect("cart_list")
    else:
        product = CartDetail.objects.filter(id=id)
        messages.error(request, "cart product not delete")


@login_required
def cart_list(request):
    user = request.user
    if request.user.is_staff:
        carts = CartDetail.objects.all()
        return render(request, "cart_list.html", {"carts": carts})
    else:
        carts = CartDetail.objects.filter(user=user)
        return render(request, "cart_list.html", {"carts": carts})


@login_required
def users_of_cart_list(request):
    user = request.user
    if user.is_staff:
        users_with_cart = CartDetail.objects.values_list(
            "user_id", flat=True
        ).distinct()
        users = UserDetail.objects.filter(id__in=users_with_cart)
        has_carts = users.exists()
        return render(
            request, "users_of_cart_list.html", {"users": users, "has_carts": has_carts}
        )


@login_required
def carts_list(request, user_id):
    user = get_object_or_404(UserDetail, id=user_id)
    orders = CartDetail.objects.filter(user=user)
    return render(request, "cart_list.html", {"carts": orders})
