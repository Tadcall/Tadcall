from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class RealPhoneNumber(models.Model):
    number = models.CharField(max_length=50)
    user = models.ForeignKey(User)

    def __str__(self):
        return "%s %s" % ( self.user, self.number)

class VirtualPhoneNumber(models.Model):
    number = models.CharField(max_length=50)
    user = models.ForeignKey(User)

    def __str__(self):
        return "%s %s" % ( self.user, self.number)

class Link(models.Model):
    user = models.ForeignKey(User)
    virtual_phone_number = models.ForeignKey(VirtualPhoneNumber)
    real_phone_number = models.ForeignKey(RealPhoneNumber)

    def __str__(self):
        return "%s %s %s" % ( self.user, self.virtual_phone_number, self.real_phone_number)
