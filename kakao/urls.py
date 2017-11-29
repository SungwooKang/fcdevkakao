from django.conf.urls import url
from . import views
from django.contrib import admin

 
urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^keyboard/', views.keyboard),
        url(r'^message', views.message),
]