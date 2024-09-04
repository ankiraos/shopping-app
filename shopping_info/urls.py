from django.urls import path
from . import views

urlpatterns = [
    # path("", views.shop, name="shop"),
    path("", views.home, name="home"),
    # register , login , logout, user
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("user-list/", views.user_list, name="user_list"),
    path("del_user", views.delete_user, name="del-user"),
    # add product, product list, del product
    path("add_product", views.add_productview, name="add_product"),
    path("products-list", views.product_list, name="product_list"),
    path("delproduct/<int:id>", views.del_product, name="del-product"),
    # add cart, cart list, del cart
    path("addcart_plist/<int:id>", views.addcart_by_plist, name="addcart_by_plist"),
    path("addcart", views.addcart_view, name="add-cart"),
    path("cart-list", views.cart_list, name="cart_list"),
    path("delcart/<int:id>", views.del_addcart, name="delcart"),
    path("users_of_cart_list", views.users_of_cart_list, name="users_of_cart_list"),
    path("carts-list/<int:user_id>/", views.carts_list, name="carts_list"),
    # order ,order list, del order
    path("order-list", views.order_list, name="order_list"),
    path("users_of_order_list", views.users_of_order_list, name="users_of_order_list"),
    path("order-detail", views.orderdetail_view, name="order_detail"),
    path("del_order/<int:id>", views.del_order, name="cancel_order"),
    path("add_order/<int:id>", views.add_order, name="add-order"),
    path("orders-list/<int:user_id>/", views.orders_list, name="orders-list"),
]
