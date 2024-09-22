from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor, Specialization, Designation, AvailableTime, Review
from .serializers import DoctorSerializer, SpecializationSerializer, DesignationSerializer, AvailableTimeSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission
from rest_framework import filters, pagination

# Create your views here.
class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 # items per page
    page_size_query_param = page_size
    max_page_size = 100

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination

class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer


class AvailableTimeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    
    

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
