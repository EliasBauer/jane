from django.db import models


class Creditor(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.IntegerField(max_length=6)
    contact_one = models.CharField(max_length=100, null=True, blank=True)
    contact_two = models.CharField(max_length=100, null=True, blank=True)
    account_number = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date = models.DateField(auto_now_add=True)
    last_payment = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Debtor(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.IntegerField(max_length=6)
    contact_one = models.CharField(max_length=100, null=True, blank=True)
    contact_two = models.CharField(max_length=100, null=True, blank=True)
    account_number = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date = models.DateField(auto_now_add=True)
    last_payment = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
