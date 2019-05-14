from django.contrib.auth.models import User
from api.serializers import CustomerSerializer, CustomerSerializer2
from api.models import Customer
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

class CustomerList(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key,
                     'username': user.username})

@api_view(['POST'])
def logout(request):
    request.auth.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerCreate(APIView):
    def post(self, request):
        serializer = CustomerSerializer2(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            if customer:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)