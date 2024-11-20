from django.db import models

class Sector(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'sector'

    def __str__(self):
        return self.name

class Usuario(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'usuario'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"