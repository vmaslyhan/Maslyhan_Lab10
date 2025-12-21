from django.db import models

class Guest(models.Model):
    guest_id = models.AutoField(primary_key=True, db_column='guest_id')
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        db_table = 'guests'


class Room(models.Model):
    room_number = models.AutoField(primary_key=True, db_column='room_number')
    num_rooms = models.IntegerField()
    floor = models.IntegerField()
    tv = models.BooleanField()
    fridge = models.BooleanField()
    num_places = models.IntegerField()
    category = models.CharField(max_length=20)
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"№{self.room_number} ({self.category})"

    class Meta:
        db_table = 'rooms'


class Registration(models.Model):
    registration_id = models.AutoField(primary_key=True, db_column='registration_id')
    guest = models.ForeignKey(
        Guest, on_delete=models.CASCADE, db_column='guest_id'
    )
    arrival_date = models.DateField()
    num_days = models.IntegerField()
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, db_column='room_number'
    )

    def __str__(self):
        return f"Registration {self.registration_id}"

    class Meta:
        db_table = 'registrations'
