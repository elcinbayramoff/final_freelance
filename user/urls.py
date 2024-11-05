from django.urls import path
from .views import RegisterUserView, OTPVerificationView, LoginUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('verify-otp/', OTPVerificationView.as_view(), name='verify-otp'),
    path('login/', LoginUserView.as_view(), name='login'),
]
