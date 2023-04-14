from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import My_ModelSerialaizer


class My_ModelAPI(generics.ListAPIView):
    queryset = My_Model.objects.all()
    serializer_class = My_ModelSerialaizer
