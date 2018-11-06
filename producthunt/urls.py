from django.contrib import admin
from django.urls import path
import products.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products.views.index, name="home"),
    
]
