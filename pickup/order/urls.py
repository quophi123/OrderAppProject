from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    
    path('sign-in/',auth_views.LoginView.as_view(template_name='sign-in.html')),
    path('sign-out/',auth_views.LogoutView.as_view(next_page='/')),
    path('sign-up/',views.sign_up,name='sign-up'),
    
    path('customer/',views.customer_page,name='customer'),
    path('courier/', views.courier_page,name='courier'),
]
