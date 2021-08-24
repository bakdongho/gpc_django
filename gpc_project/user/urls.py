from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import UserRegistrationView, UserLoginView, UserVerificationView, ResendVerifyEmailView

urlpatterns = [
    path('create', UserRegistrationView.as_view(), name='userRegistration'),
    path('<user_pk>/verify/<email_token>', UserVerificationView.as_view(), name='userVerification'),
    path('resend_verify_email', ResendVerifyEmailView.as_view(), name='resendVerifyEmail'),
    path('login', UserLoginView.as_view(), name='userLogin'),
    path('logout', LogoutView.as_view(), name='userLogout'),
]
