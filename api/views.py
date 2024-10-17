from django.shortcuts import render
from .serializer import ProfileSerializer
from .models import profile
from rest_framework import viewsets
# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = profile.objects.all()
    serializer_class = ProfileSerializer
