from rest_framework import serializers
from .models import Carrera, Lead, Materia


class LeadSerializer(serializers.ModelSerializer):
    
    class Meta:
            model = Lead
            fields = ('__all__')


class MateriaSerializer(serializers.ModelSerializer):
    
    class Meta:
            model = Materia
            fields = ('__all__')


class CarreraSerializer(serializers.ModelSerializer):
    
    class Meta:
            model = Carrera
            fields = ('__all__')