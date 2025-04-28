from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from .serializers import ReviewSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.exceptions import NotFound



class ReviewListView(APIView):
    http_method_names = ['get', 'post']
    @swagger_auto_schema(operation_description="Get all reviews")
    def get(self, request, *args, **kwargs):
        reviews = Review.objects.filter(service_id=kwargs.get('service_id'))
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Create a new review", request_body=ReviewSerializer)
    def post(self, request, *args, **kwargs):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ReviewDetailView(APIView):
    http_method_names = ['get', 'put']
    @swagger_auto_schema(operation_description="Get one review")
    def get(self, request, *args, **kwargs):
        review = Review.objects.get(pk=kwargs.get('pk'))
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="update one review", request_body=ReviewSerializer)
    def put(self, request, *args, **kwargs):
        review = Review.objects.get(pk=kwargs.get('pk'))
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def put(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)

    # @swagger_auto_schema(operation_description="delete an existing review", request_body=ReviewSerializer)
    # def delete(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)