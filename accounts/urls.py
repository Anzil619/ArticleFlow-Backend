from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *



urlpatterns = [

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', GetUpdateProfile.as_view(), name='profile'),
    path('changepassword/', ChangePassword.as_view(), name='changepassword'),

]