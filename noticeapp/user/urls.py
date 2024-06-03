from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView, PasswordResetView, OTPVerifyView,PasswordUpdateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('passwordReset/', PasswordResetView.as_view(), name='password_reset'),
    path('otpVerify/', OTPVerifyView.as_view(), name='otp_verify'),
    path('passwordUpdate/', PasswordUpdateView.as_view(), name='password_update'),
]