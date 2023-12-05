
from django.urls import path
from .views import *


urlpatterns = [
    path('sign-up/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('forgot-password/', ForgotPasswordView.as_view()),
    path('update-account/', UpdateAccountView.as_view()),
    path('delete-account/', DeleteAccountView.as_view()),
]
