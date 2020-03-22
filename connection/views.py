from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny


class ConnectionViewSet(generics.CreateAPIView):
    permission_classes = [AllowAny]
