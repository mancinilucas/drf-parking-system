from django.db import models


class Commercial_Establishment(models.Model):
    name = models.CharField(max_length=100, blank=False)
    cnpj = models.CharField(max_length=14, blank=False)
    adress = models.CharField(max_length=100, blank=False)
    phone = models.IntegerField(max_length=14, blank=False)
    car_parking_spaces = models.IntegerField(max_length=100, blank=False)
    motorcycle_parking_spaces = models.IntegerField(
        max_length=100, blank=False)

    def __str__(self):
        return f'Nome do estabelecimento: {self.name} | CNPJ: {self.cnpj}'


class Vehicle(models.Model):
    brand = models.CharField(max_length=50, blank=False)
    model = models.CharField(max_length=50, blank=False)
    color = models.CharField(max_length=20, blank=False)
    car_plate = models.CharField(max_length=7, blank=False)
    type = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return f'Marca: {self.brand} | Modelo: {self.model} | Cor: {self.color} | Placa: {self.car_plate} | Tipo: {self.type}'
