from django.contrib.auth.models import AbstractUser

from django.db import models


class CustomUser(AbstractUser):
    pass


class AirplaneManager(models.Manager):
    def create(self, *args, **kwargs):
        print(kwargs)
        if not kwargs.get('fuel_capacity'):
            fuel_capacity = kwargs.get('id', 0) * 200
            kwargs['fuel_capacity'] = fuel_capacity
        if not kwargs.get('base_fuel_consumption'):
            base_fuel_consumption = kwargs.get('id', 0) * 0.8
            kwargs['base_fuel_consumption'] = base_fuel_consumption
        return super(AirplaneManager, self).create(*args, **kwargs)


class Airplane(models.Model):
    id = models.PositiveIntegerField(unique=True, primary_key=True, blank=False, null=False)
    passengers = models.PositiveIntegerField(null=False, blank=False, default=0)

    name = models.CharField(max_length=120, blank=True, null=True, )
    base_fuel_capacity = models.FloatField(blank=True, default=0.0)
    base_fuel_consumption = models.FloatField(blank=True, default=0.0)

    passenger_capacity = models.IntegerField(blank=True, null=True)

    objects = AirplaneManager()
