from rest_framework import viewsets, views

from data_app.serializers import WindSerializer, RotorSerializer, EletricPowerSerializer
from data_app.models import Wind, Rotor, EletricPower

import csv
import zipfile

from django.http import HttpResponse


class WindViewSet(viewsets.ModelViewSet):
    queryset = Wind.objects.all().order_by('creation_date')
    serializer_class = WindSerializer

class RotorViewSet(viewsets.ModelViewSet):
    queryset = Rotor.objects.all().order_by('creation_date')
    serializer_class = RotorSerializer

class EletricPowerViewSet(viewsets.ModelViewSet):
    queryset = EletricPower.objects.all().order_by('creation_date')
    serializer_class = EletricPowerSerializer

class BackupView(views.APIView):
    def get(self, request):
        response = HttpResponse(
            content_type='application/zip',
            headers={'Content-Disposition': 'attachment; filename="backup.zip"'},
        )

        with open('wind-backup.csv', 'w', encoding='UTF8', newline='') as file:
            writer = csv.writer(file)

            for wind in Wind.objects.all():
                wind_speed_string = str(wind.wind_speed)
                wind_creation_date_string = wind.creation_date.__str__()

                writer.writerow([wind_speed_string, wind_creation_date_string])

        with open('rotor-backup.csv', 'w', encoding='UTF8', newline='') as file:
            writer = csv.writer(file)

            for rotor in Rotor.objects.all():
                rotor_speed_string = str(rotor.rotor_speed)
                rotor_creation_date_string = rotor.creation_date.__str__()

                writer.writerow([rotor_speed_string, rotor_creation_date_string])

        with open('eletric-power-backup.csv', 'w', encoding='UTF8', newline='') as file:
            writer = csv.writer(file)

            for eletric_power in EletricPower.objects.all():
                energy_production_string = str(eletric_power.energy_production)
                eletric_power_creation_date_string = eletric_power.creation_date.__str__()

                writer.writerow([energy_production_string, eletric_power_creation_date_string])

        zip_file = zipfile.ZipFile(response, 'w')

        for filename in ['wind-backup.csv', 'rotor-backup.csv', 'eletric-power-backup.csv']:
            zip_file.write(filename)

        return response
