from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^ourprojects/$', views.ourprojects, name='ourprojects'),
    url(r'^careers/$', views.jobs, name='careers'),
    url(r'^dammi/$', views.dammi, name='dammi'),
    ]