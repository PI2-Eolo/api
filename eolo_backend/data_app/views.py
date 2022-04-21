from rest_framework import viewsets

from data_app.serializers import WindSerializer, RotorSerializer, EletricPowerSerializer
from data_app.models import Wind, Rotor, EletricPower

class WindViewSet(viewsets.ModelViewSet):
    queryset = Wind.objects.all().order_by('creation_date')
    serializer_class = WindSerializer

class RotorViewSet(viewsets.ModelViewSet):
    queryset = Rotor.objects.all().order_by('creation_date')
    serializer_class = RotorSerializer

class EletricPowerViewSet(viewsets.ModelViewSet):
    queryset = EletricPower.objects.all().order_by('creation_date')
    serializer_class = EletricPowerSerializer
