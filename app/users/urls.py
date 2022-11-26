from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
# 登录拦截
app_name = "users"

urlpatterns = [
    path("login/", views.log_in.as_view(), name="login"),
    path("logout/", views.log_out.as_view(), name="logout")
]