from django.db import models

import json

class User(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def to_json(self):
        return json.dumps({
            'user': self.id,
            'name': self.name
        })

class RealPhoneNumber(models.Model):
    number = models.CharField(max_length=50)
    user = models.ForeignKey(User)

    def __str__(self):
        return "%s %s" % ( self.user, self.number)

    def to_json(self):
        return json.dumps({
            'type': 'real',
            'number': number,
            'user': user.to_json()
        })


class VirtualPhoneNumber(models.Model):
    number = models.CharField(max_length=50)
    user = models.ForeignKey(User)

    def __str__(self):
        return "%s %s" % ( self.user, self.number)

    def to_json(self):
        return json.dumps({
            'type': 'virtual',
            'number': self.number,
            'user': user.to_json()
        })

class Link(models.Model):
    user = models.ForeignKey(User)
    virtual_phone_number = models.ForeignKey(VirtualPhoneNumber)
    real_phone_number = models.ForeignKey(RealPhoneNumber)

    def __str__(self):
        return "%s %s %s" % ( self.user, self.virtual_phone_number, self.real_phone_number)

    def to_json(self):
       return  json.dump({
           user: user.to_json(),
           real_phone_number: real_phone_number.to_json(),
           virtual_phone_number: virtual_phone_number.to_json()
       })

