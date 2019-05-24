from . import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    url(r'^new/', views.index, name="make it short"),
    url(r'^(?P<page_alias>.+?)/$', views.get_original, name="get original"),

]
