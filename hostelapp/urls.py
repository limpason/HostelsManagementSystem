
from django.contrib import admin
from django.urls import path
from hostelapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('aboutus', views.aboutus),
    path('products', views.products),
    path('form', views.form),
]
