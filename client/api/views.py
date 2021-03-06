from django.contrib.auth.models import User
from django.http import Http404
# from django.shortcuts import get_object_or_404
from .serializers import (UserSerializer,
                        UserDetailSerializer, 
                        UserCreateSerializer,
                        UserLoginSerializer,
                        ProfileSerializer)

from rest_framework.response import Response 
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT 
from rest_framework.views import APIView 

from rest_framework import viewsets
from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView,
                                    RetrieveAPIView,)


from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from django.contrib.auth import get_user_model
User = get_user_model()

class UserListView(ListAPIView):
    """
    API for list of users for admin.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class UserDetailView(APIView):
    """
    Retrieve, update a user instance.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserDetailSerializer

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = UserDetailSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserDetailSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


   
class UserCreateAPIView(CreateAPIView):
    """
    API for register of users.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserCreateSerializer


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer


    def post(self, request, *args, **kwargs):
        data =  request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


