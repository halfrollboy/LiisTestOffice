from django.contrib import admin
from django.contrib.admin import ModelAdmin

from cabinets.models import Cabinet, Seat, Reservation


@admin.register(Cabinet)
class CabinetAdmin(ModelAdmin):
    pass


@admin.register(Seat)
class SeatAdmin(ModelAdmin):
    pass


@admin.register(Reservation)
class ReserveAdmin(ModelAdmin):
    pass
