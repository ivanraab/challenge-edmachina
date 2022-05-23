from django.urls import path, include
from rest_framework import routers
from leads.views import LeadViewSet, MateriaViewSet, CarreraViewSet

router = routers.DefaultRouter()
router.register('leads', LeadViewSet, basename='leads')
router.register('materias', MateriaViewSet, basename='materias')
router.register('carreras', CarreraViewSet, basename='carreras')

urlpatterns = [
    path('', include(router.urls)),

]