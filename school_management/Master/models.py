from django.db import models

# Create your models here.
class CountryMaster(models.Model):
    country_name = models.CharField(max_length = 50)

class UserMaster(models.Model):
    user_type = models.CharField(max_length = 50)

class ReferalMaster(models.Model):
    referal_type = models.CharField(max_length = 10)

class StateMaster(models.Model):
    state_name = models.CharField(max_length = 50)

class BankMaster(models.Model):
    bank_name = models.CharField(max_length = 50)

class GenderMaster(models.Model):
    gender_type = models.CharField(max_length = 15)

class DocumentMaster(models.Model):
    document_type = models.CharField(max_length = 50)
