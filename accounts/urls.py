from accounts import views as users_views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import (
    UserSignupAPIView
)

urlpatterns = [
    # url('home/', users_views.home, name='home'),
    url(r'^register/$', UserSignupAPIView.as_view(), name='register'),
    url('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
]