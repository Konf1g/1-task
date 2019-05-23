from . import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    url(r'^new/', views.index, name="make it short"),
    # path('new/', views.index, name="make it short"),

]
