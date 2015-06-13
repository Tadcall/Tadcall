from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)


class RealPhoneNumber(models.Model):
    number = models.CharField(max_length=50)
    user = models.ForeignKey(User)

class VirtualPhoneNumber(models.Model):
    number = models.CharField(max_length=50)
    user = models.ForeignKey(User)
