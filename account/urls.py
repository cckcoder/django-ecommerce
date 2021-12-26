from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.views.generic.base import TemplateView

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
    path(
        "password_reset",
        auth_views.PasswordResetView.as_view(
            template_name="account/user/password_reset_form.html",
            success_url="password_reset_email_confirm",
            email_template_name="account/user/password_reset_email.html"
        ),
    ),
    path("dashboard", views.dashboard, name="dashboard"),
    path("profile/edit/", views.edit_details, name="edit_details"),
    path("profile/delete_user/", views.delete_user, name="delete_user"),
    path(
        "profile/delete_confirm/",
        TemplateView.as_view(template_name="account/user/delete_confirm.html"),
        name="delete_confirmation",
    ),
]
