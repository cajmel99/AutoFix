from django.urls import path
from .views import ReviewListView, ReviewDetailView

urlpatterns = [
    # Endpoint dla listy opinii
    path('<str:service_id>/', ReviewListView.as_view(), name='review-list'),

    # Endpoint dla pojedynczej opinii
    path('<str:service_id>/<str:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]