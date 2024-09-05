from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Commercial_Establishment, Vehicle
from .serializers import CommercialEstablishmentSerializer, VehicleSerializer


@api_view(['GET'])
def get_all_establishments(request):
    if request.method == 'GET':
        establishments = Commercial_Establishment.objects.all()
        serializer = CommercialEstablishmentSerializer(
            establishments, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)
