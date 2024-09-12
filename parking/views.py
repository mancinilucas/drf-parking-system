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


@api_view(['GET', 'POST'])
def get_vehicles(request):
    if request.method == 'GET':
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(
            vehicles, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        vehicle_serializer = VehicleSerializer(
            data=request.data)
        if vehicle_serializer.is_valid():
            vehicle_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response({'error': 'Vehicle not created'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def vehicle_manager(request, id):
    try:
        vehicle = Vehicle.objects.get(pk=id)
    except Vehicle.DoesNotExist:
        return Response({'error': 'Vehicle not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        vehicle_serializer = VehicleSerializer(
            vehicle)
        return Response(vehicle_serializer.data)

    elif request.method == 'PUT':
        vehicle_serializer = VehicleSerializer(
            vehicle, data=request.data)
        if vehicle_serializer.is_valid():
            vehicle_serializer.save()
            return Response(vehicle_serializer.data)
        return Response({'error': 'Vehicle not updated'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
