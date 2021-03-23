
from django.urls import path,include
from . import views



urlpatterns = [
    path('donator',views.donator,name="donator"),
    path('register',views.register,name="register")
]