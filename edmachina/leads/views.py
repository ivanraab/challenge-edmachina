from django.shortcuts import render

from .serializers import LeadSerializer, MateriaSerializer, CarreraSerializer
from .models import Lead, Materia, Carrera
from rest_framework import serializers, mixins, viewsets


# class LeadViewSet(mixins.ListModelMixin,
#                     mixins.RetrieveModelMixin,
#                     mixins.CreateModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     viewsets.GenericViewSet):

class LeadViewSet(viewsets.ModelViewSet):

    queryset = Lead.objects.all().order_by('id')
    filter_fields = ('__all__')
    serializer_class = LeadSerializer


class MateriaViewSet(viewsets.ModelViewSet):

    queryset = Materia.objects.all().order_by('id')
    filter_fields = ('__all__')
    serializer_class = MateriaSerializer


class CarreraViewSet(viewsets.ModelViewSet):

    queryset = Carrera.objects.all().order_by('id')
    filter_fields = ('__all__')
    serializer_class = CarreraSerializer