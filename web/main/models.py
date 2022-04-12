from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)


class Airplane(models.Model):
    fuel_tank = models.IntegerField()
    consumption = models.IntegerField()


class CompanyAirplanes(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='company_airplane'
    )
    airplane = models.ForeignKey(
        Airplane,
        on_delete=models.SET_NULL,
        related_name='airplane_of_company',
        null=True
    )
