from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from mainapp.models import PodcastModel, PodcasterModel, ContactModel
from .serializers import PodcastSerializer, PodcasterSerializer, LoginSerializer, ContactSerializer

# display podcasts api
class PodcastListView(ListCreateAPIView):
    queryset = PodcastModel.objects.all()
    serializer_class = PodcastSerializer
    permission_class = IsAdminUser

# display Podcasters api
class PodcasterDetailView(RetrieveDestroyAPIView):
    queryset = PodcasterModel.objects.all()
    serializer_class = PodcasterSerializer
    permission_class = IsAdminUser

# Login from api 
class LoginRegisterView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            if 'username' in data:
                User.objects.create_user(data['username'], data['email'], data['password'])
            if 'username' in data:
                username = data['username']
                password = data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return Response({'success': True})
                else:
                    return Response({'success': False, 'message': 'Invalid credentials'})
        else:
            raise ParseError(serializer.errors)

# Logout from api
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        logout(request)
        return Response({"message": "You have successfully logged out."})

# comments to api
class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer