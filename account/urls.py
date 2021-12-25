from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings

from . import views
from account.forms import UserLoginForm

app_name = "account"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="account/registration/login.html", form_class=UserLoginForm
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page=settings.LOGIN_URL),
        name="logout",
    ),
    path("register/", views.account_register, name="register"),
    path(
        "activate/<slug:uidb64>/<slug:token>/", views.account_activate, name="activate"
    ),
    path("dashboard", views.dashboard, name="dashboard"),
    path("profile/edit/", views.edit_details, name="edit_details"),
    # path("profile/delete_user/", views.delete_user, name="delete_user"),
]
