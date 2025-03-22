from django.urls import path
from .views import *
urlpatterns = [
    path("",homepage,name="homepage"),
    path("a2c/<str:product_id>/",addtocart,name="a2c"),
    path("vucart",viewcart,name="viewcart"),
    path("clear/<int:product_id>",clear,name="clear"),
    path("updateqty/<int:product_id>/<str:action>",updateqty,name="updateqty"),
    path("clearcart/<str:action>",cartclear,name="cartclear"),
]
