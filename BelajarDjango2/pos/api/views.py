
from warnings import filters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pos_app.models import StatusModel, Category, MenuResto
from django.contrib.auth.models import User
from .serializers import (
    LoginSerializer,
    RegisterUserSerializer,
    MenuRestoSerializer
)
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .paginators import CustomPagination
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import filters

#untuk buat endpoint register, buat bikin akun admin
class RegisterUserAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer

    def post(self, request, format = None):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()

            response_data = {
                'status' : status.HTTP_201_CREATED,
                'message' : 'Selamat anda telah terdaftar...',
                'data' : serializer.data
            }

            return Response(response_data, status = status.HTTP_201_CREATED)

        return Response({
            'status' : status.HTTP_400_BAD_REQUEST,
            'data' : serializer.errors,
            'status' : status.HTTP_400_BAD_REQUEST
        })

class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        user = serializer.validated_data['user']

        django_login(request, user)

        token, created = Token.objects.get_or_create(user = user)

        return Response({
            'status' : 200,
            'message' : 'Selamat anda berhasil masuk...',
            'data' : {
                'token' : token.key,
                'id' : user.id,
                'first_name' : user.first_name,
                'last_name' : user.last_name,
                'email' : user.email,
                'is_active' : user.is_active,
            }
        })

class MenuRestoView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        menu_restos = MenuResto.objects.select_related('status') \
            .filter(status = StatusModel.objects.first())

        serializer = MenuRestoSerializer(menu_restos, many = True)

        response = {
            'status' : status.HTTP_200_OK,
            'message' : 'Pembacaan seluruh data berhasil...',
            'user' : str(request.user),
            'auth' : str(request.auth),
            'data' : serializer.data,
        }

        return Response(response, status = status.HTTP_200_OK)


class MenuRestoFilterApi(generics.ListAPIView):
    queryset = MenuResto.objects.all()
    serializer_class = MenuRestoSerializer
    pagination_class = CustomPagination
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['category__name']
    ordering_fields = ['created_on']