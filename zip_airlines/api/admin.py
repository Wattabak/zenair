from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api.models import Airplane
from api.models import CustomUser


@admin.register(Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'passengers',
        'name',
        'base_fuel_capacity',
        'base_fuel_consumption',
        'passenger_capacity'
    )
    fields = (
        'id',
        'passengers',
        'name',
        'base_fuel_capacity',
        'base_fuel_consumption',
        'passenger_capacity'
    )

    def save_model(self, request, obj, form, change):
        if change:
            obj.save()
        else:
            print(form.cleaned_data)
            new_obj = Airplane.objects.create(**form.cleaned_data)
            obj.id = new_obj.id


admin.site.register(CustomUser, UserAdmin)
