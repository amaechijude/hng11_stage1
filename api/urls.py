from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('api/hello', views.hello, name='hello'),
]
