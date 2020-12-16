"""Eshopproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Eshop import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('signup/',views.register,name="reg"),

    path('my_products/',views.my_products,name="my_products"),
    path("sendemail",views.sendemail, name="sendemail"),
    path('single_product/>',views.single_product, name="single_product"),
    path('update_product/',views.update_product, name="update_product"),
    path('delete_product/',views.delete_product, name="delete_product"),
    path('all_products/',views.all_products, name="all_products"),

    path("forgotpass",views.forgotpass, name="forgotpass"),
    path("reset_password",views.reset_password,name="reset_password"),
    path('change_password/',views.change_password,name="change_password"),
    path('edit_profile/',views.edit_profile,name="edit_profile"),
    path('cust_dashboard/',views.cust_dashboard,name="cust_dashboard"),
    path('sell_dashboard/',views.sell_dashboard,name="sell_dashboard"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('add_product/',views.add_product_view,name='add_product_view'),

     path("cart",views.add_to_cart,name="cart"),
    path("get_cart_data",views.get_cart_data,name="get_cart_data"),
    path("change_quan",views.change_quan,name="change_quan"),

    #path('paypal/', include('paypal.standard.ipn.urls')),
    path('process_payment',views.process_payment,name="process_payment"),
    path('payment_done',views.payment_done,name="payment_done"),
    path('payment_cancelled',views.payment_cancelled,name="payment_cancelled"),
    path('order_history',views.order_history,name="order_history"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
