from django.urls import path
from .views import ServiceReviewListView, ReviewDetailView, MechanicReviewListView, MyReviewListView, MechanicRaitingView
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     # Endpoint dla listy opinii
#     path('<str:service_id>/', ServiceReviewListView.as_view(), name='review-list'),
#
#     path('<int:mechanic_id>/',MechanicReviewListView.as_view(), name="reviews-by-mechanic"),
#     # Endpoint dla pojedynczej opinii
#     path('<str:service_id>/<str:pk>/', ReviewDetailView.as_view(), name='review-detail'),
# ]

urlpatterns = [
    # 1. Moje recenzje (tylko GET listy)
    path(
        'me/',
        MyReviewListView.as_view(),
        name='reviews-me-list'
    ),
    # 2. Szczegóły / edycja / usuwanie mojej recenzji (GET, PUT, DELETE)
    path(
        'me/<int:pk>/',
        ReviewDetailView.as_view(),
        name='reviews-me-detail'
    ),
    # 5. Lista recenzji dla danej usługi (GET) i tworzenie nowej recenzji (POST)
    path(
        'service/<int:service_id>/reviews/',
        ServiceReviewListView.as_view(),
        name='reviews-service-list-create'
    ),
    # 3. Lista recenzji dla danego mechanika (GET)
    path(
        'mechanic/<int:mechanic_id>/reviews/',
        MechanicReviewListView.as_view(),
        name='reviews-mechanic-list'
    ),
    # 4. Średnia ocena mechanika (GET)
    path(
        'mechanic/<int:mechanic_id>/rating/',
        MechanicRaitingView.as_view(),
        name='reviews-mechanic-rating'
    ),
]