from django.urls import path
from .views import PaymentListView, PaymentDetailView

# urlpatterns = [
#     path('', PaymentViews.as_view(), name='payment-list'),
#     path('<int:id>/', PaymentViews.as_view(), name='payment-detail'),
# ]
urlpatterns = [
    # Endpoint dla listy płatności
    path('', PaymentListView.as_view(), name='payment-list'),

    # Endpoint dla pojedynczej płatności
    path('<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
]