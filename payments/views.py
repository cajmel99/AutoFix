from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.exceptions import NotFound
#
# class PaymentViews(APIView):
#     @swagger_auto_schema(operation_description="Get all payments")
#     def get(self, request, *args, **kwargs):
#         payments = Payment.objects.all()
#         serializer = PaymentSerializer(payments, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     @swagger_auto_schema(operation_description="Create a new payment", request_body=PaymentSerializer)
#     def post(self, request, *args, **kwargs):
#         serializer = PaymentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     @swagger_auto_schema(operation_description="Update an existing payment", request_body=PaymentSerializer)
#     def put(self, request, *args, **kwargs):
#         payment_id = kwargs.get('id')
#
#         try:
#             payment = Payment.objects.get(id=payment_id)
#         except Payment.DoesNotExist:
#             raise NotFound("Payment not found")
#
#         serializer = PaymentSerializer(payment, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Payment
# from .serializers import PaymentSerializer

class PaymentListView(APIView):
    http_method_names = ['get', 'post']
    @swagger_auto_schema(operation_description="Get all payments")
    def get(self, request, *args, **kwargs):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Create a new payment", request_body=PaymentSerializer)
    def post(self, request, *args, **kwargs):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PaymentDetailView(APIView):
    http_method_names = ['get', 'put']
    @swagger_auto_schema(operation_description="Get one payments")
    def get(self, request, *args, **kwargs):
        payment = Payment.objects.get(pk=kwargs.get('pk'))
        serializer = PaymentSerializer(payment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Update an existing payment", request_body=PaymentSerializer)
    def put(self, request, *args, **kwargs):
        payment = Payment.objects.get(pk=kwargs.get('pk'))
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)