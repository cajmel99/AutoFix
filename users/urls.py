from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, CustomTokenObtainPairView, ProfileUpdateView, ChangePasswordView, MeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # <-- updated
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += [
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('password/change/', ChangePasswordView.as_view(), name='password_change'),
]

urlpatterns += [
    path('me/', MeView.as_view(), name='user_detail'),
]
