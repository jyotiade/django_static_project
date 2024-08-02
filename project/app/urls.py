from django.urls import path
from .views import home
from .views import products
from .views import shops


urlpatterns = [
    path('home/',home,name="home"),
    path('products/',products,name="products"),
    path('shops/',shops,name="shops")
]