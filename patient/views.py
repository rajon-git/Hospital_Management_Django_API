from django.shortcuts import render
from .models import Patient
from .serializers import PatientSerializer, RegistrationSerializer
from rest_framework import viewsets
from rest_framework.views import APIView

# Create your views here.

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class UserRegistrationApiView(APIView):
    serializer_class = RegistrationSerializer
