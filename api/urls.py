from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('api/hello/visitor_name=<str:visitor_name>', views.hello, name='hello'),
]
