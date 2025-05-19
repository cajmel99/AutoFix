from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from .models import Review, Service
from rest_framework import viewsets
from .serializers import ReviewSerializer, ReviewCreateUpdateSerializer, ReviewSerializerMechanic
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from django.db.models import Avg


class ServiceReviewListView(APIView):
    # lista opinii dla danej usługi
    http_method_names = ['get', 'post']

    #dodanie autentykacji dla POST
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @swagger_auto_schema(operation_description="Get all reviews for service")
    def get(self, request, *args, **kwargs):
        reviews = Review.objects.filter(service_id=kwargs.get('service_id'))
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Create a new review", request_body=ReviewSerializer)
    def post(self, request, *args, **kwargs):
        service_id = kwargs.get('service_id')
        #serializer zeby nie dało się zmienić service_id usera itp
        serializer = ReviewCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                user=request.user,
                service_id=service_id
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetailView(APIView):
    # szczegóły opinii
    http_method_names = ['get']
    @swagger_auto_schema(operation_description="Get one review")
    def get(self, request, *args, **kwargs):
        review = Review.objects.get(pk=kwargs.get('pk'))
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # @swagger_auto_schema(operation_description="update one review", request_body=ReviewSerializer)
    # def put(self, request, *args, **kwargs):
    #     review = Review.objects.get(pk=kwargs.get('pk'))
    #     serializer = ReviewSerializer(review, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # # def put(self, request, *args, **kwargs):
    # #     return super().update(request, *args, **kwargs)
    #
    # @swagger_auto_schema(operation_description="delete an existing review", request_body=ReviewSerializer)
    # def delete(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

class MechanicReviewListView(APIView): #
    # lista opinii dla danego mechanika
    http_method_names = ['get']

    @swagger_auto_schema(
        operation_description="Get all reviews for a given mechanic",
        responses={200: ReviewSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        mechanic_id = kwargs.get('mechanic_id')
        # Pobieramy wszystkie recenzje, których usługa należy do tego mechanika
        reviews = Review.objects.filter(service__mechanic_id=mechanic_id).select_related('service', 'user')
        serializer = ReviewSerializerMechanic(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MyReviewListView(APIView):
    # lista opinii wystawionych przez zalogowanego użytkownika
    http_method_names = ['get', 'put', 'delete']

    permission_classes = [permissions.IsAuthenticated]
    @swagger_auto_schema(
        operation_description="Get all reviews created by the authenticated user",
        responses={200: ReviewSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        #  Pobierz tylko recenzje aktualnie zalogowanego
        reviews = Review.objects.filter(user=request.user)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="update one review", request_body=ReviewSerializer)
    def put(self, request, *args, **kwargs):
        #tu moze być problem bo api nie zwraca id tylko guid, front nie ma id
        review = get_object_or_404(Review, pk=kwargs.get('pk'))
        #sprawdzanie uprawnień
        if review.user != request.user:
            return Response({'detail': 'Brak uprawnień.'}, status=403)
        #serializer zeby nie dało się zmienić service_id usera itp
        serializer = ReviewCreateUpdateSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(operation_description="delete an existing review", request_body=ReviewSerializer)
    def delete(self, request, *args, **kwargs):
        review = get_object_or_404(Review, pk=kwargs.get('pk'))
        #to dadałem wyrzuca kod z brakiem uprawnień
        if review.user != request.user:
            return Response({'detail': 'Brak uprawnień.'}, status=403)
        review.delete()
        return Response({"detail": "Review deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class MechanicRaitingView(APIView):
    pass
    http_method_names = ['get']

    @swagger_auto_schema(operation_description="Get raiting for a given mechanic")
    def get(self, request, *args, **kwargs):
        mechanic_id = kwargs['mechanic_id']
        avg = ( Review.objects.filter(service__mechanic_id=mechanic_id)
                .aggregate(average=Avg('note'))['average']
                or 0.0)
        return Response({'average_rating': round(avg, 1)}, status=status.HTTP_200_OK)
