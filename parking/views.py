from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Commercial_Establishment, Vehicle
from .serializers import CommercialEstablishmentSerializer, VehicleSerializer


@api_view(['GET', 'POST'])
def get_establishments(request):
    if request.method == 'GET':
        establishments = Commercial_Establishment.objects.all()
        serializer = CommercialEstablishmentSerializer(
            establishments, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        establishment_serializer = CommercialEstablishmentSerializer(
            data=request.data)
        if establishment_serializer.is_valid():
            establishment_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response({'error': 'Establishment not created'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def establishment_manager(request, id):
    try:
        establishment = Commercial_Establishment.objects.get(pk=id)
    except Commercial_Establishment.DoesNotExist:
        return Response({'error': 'Establishment not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        establishment_serializer = CommercialEstablishmentSerializer(
            establishment)
        return Response(establishment_serializer.data)

    elif request.method == 'PUT':
        establishment_serializer = CommercialEstablishmentSerializer(
            establishment, data=request.data)
        if establishment_serializer.is_valid():
            establishment_serializer.save()
            return Response(establishment_serializer.data)
        return Response({'error': 'Establishment not updated'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        establishment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
