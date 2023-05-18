from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('customer/',views.customer_page,name='customer'),
    path('courier/', views.courier_page,name='courier'),
]
