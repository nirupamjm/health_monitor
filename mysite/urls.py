from django.contrib import admin
from django.urls import path, include
from . import views
from main import views as main_views 
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"), 
    path('', main_views.home, name='home'), 
]