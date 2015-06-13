from django.db import models

import json

class User(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'user_id': self.id,
            'name': self.name
        }

class RealPhoneNumber(models.Model):
    number = models.CharField(max_length=50)
    user = models.ForeignKey(User)

    def __str__(self):
        return "%s %s" % ( self.user, self.number)

    def to_dict(self):
        return {
            'type': 'real',
            'number': self.number,
            'user': self.user.to_dict()
        }


class VirtualPhoneNumber(models.Model):
    number = models.CharField(max_length=50)
    user = models.ForeignKey(User)

    def __str__(self):
        return "%s %s" % ( self.user, self.number)

    def to_dict(self):
        return {
            'type': 'virtual',
            'number': self.number,
            'user': self.user.to_dict()
        }

class Link(models.Model):
    user = models.ForeignKey(User)
    virtual_phone_number = models.ForeignKey(VirtualPhoneNumber)
    real_phone_number = models.ForeignKey(RealPhoneNumber)

    def __str__(self):
        return "%s %s %s" % ( self.user, self.virtual_phone_number, self.real_phone_number)

    def to_dict(self):
       return  {
           'user': self.user.to_dict(),
           'real_phone_number': self.real_phone_number.to_dict(),
           'virtual_phone_number': self.virtual_phone_number.to_dict()
       }

