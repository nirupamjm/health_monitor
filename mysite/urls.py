from django.contrib import admin
from django.urls import path, include
from . import views
from main import views as main_views 
from register import views as v
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"), 
    path('home', main_views.home, name='home'), 
    path('', main_views.home, name='home'),
    path('', include("django.contrib.auth.urls")),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
