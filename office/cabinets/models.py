from django.contrib.auth.models import User
from django.db import models


class Cabinet(models.Model):
    name = models.CharField("Название кабинета", max_length=255)
    seats = models.IntegerField("Количество мест в кабинете")

    def __str__(self):
        return f'{self.id}:{self.name}'


class Seat(models.Model):
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE, related_name='cabinet_seat')
    reservation_time = models.ManyToManyField(User, through='Reservation', related_name='seat')

    def __str__(self):
        return f'Кресто id{self.id}: в кабинете № "{self.cabinet.name}"'


class Reservation(models.Model):
    datetime_from = models.DateTimeField("Занято с")
    datetime_to = models.DateTimeField("Занято по")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

    def __str__(self):
        return f'Кресто id{self.seat.id}: в кабинете № "{self.seat.cabinet.name}" зарезервировано с ' \
            f'{self.datetime_from} по {self.datetime_to}'
