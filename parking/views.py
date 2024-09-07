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


@api_view(['GET'])
def get_establishment_by_id(request, id):
    if request.method == 'GET':
        try:
            establishment = Commercial_Establishment.objects.get(pk=id)
        except Commercial_Establishment.DoesNotExist:
            return Response({'error': 'Establishment not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = CommercialEstablishmentSerializer(establishment)
    return Response(serializer.data)
