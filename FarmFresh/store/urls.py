from django.urls import path
from . views import *
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', store, name="store"),
	path('cart/', cart, name="cart"),
	path('checkout/', checkout, name="checkout"),

	path('update_item/', updateItem, name='update_item'),
	path('process_order/', processOrder, name='process_order'),



	path('login/', login, name='login'),
    path('signup/', signUp, name='signUp'),
    path('activate/<uidb64>/<token>/', activate, name="activate"),
    path(
        'confirmation-sent/',
        TemplateView.as_view(template_name="confirmation_sent.html"),
        name="confirmation_sent",
    ),
    path(
        'activation-complete/',
        TemplateView.as_view(template_name="activation_complete.html"),
        name="activation_complete",
    ),
    path(
        "activation-invalid/",
        TemplateView.as_view(template_name="activation_invalid.html"),
        name="activation_invalid",
    ),
    path(
        "reset-password/",
        auth_views.PasswordResetView.as_view(template_name="reset_password.html"),
        name="reset_password",
    ),
    path(
        "reset-password-sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password_reset_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset_form.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path("logout/", logout, name="logout"),

]