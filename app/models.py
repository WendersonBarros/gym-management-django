from django.db import models


class Membership(models.Model):
    name = models.CharField(max_length=200)
    duration_in_months = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    entry_code = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class Membership_status(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    current_membership = models.ForeignKey(Membership, on_delete=models.RESTRICT)
    expiration_date = models.DateField()
