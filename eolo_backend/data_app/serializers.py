from rest_framework import serializers

from data_app.models import Wind, Rotor, EletricPower

class WindSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wind
        fields = ['wind_speed', 'creation_date']

class RotorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rotor
        fields = ['rotor_speed', 'creation_date']

class EletricPowerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EletricPower
        fields = ['energy_production', 'creation_date']
