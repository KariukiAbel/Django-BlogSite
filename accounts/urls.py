from django.conf.urls import url
from django.urls import path
from . import views

#name space
app_name = 'accounts'

urlpatterns = [
path(r'signup/', views.signup_view, name='signup'),
path(r'login/', views.login_view, name='login'),
path(r'logout/', views.logout_view, name='logout'),
]
