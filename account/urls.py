from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^$', views.home, name='home'),
    url(r'^registration/$', views.RegisterFormView.as_view(), name='registration'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^password/$', views.ChangePasswordView, name='change_password'),
]