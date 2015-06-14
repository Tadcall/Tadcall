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
        timeRestrictions = TimeRestriction.objects.filter(link = self.id)
        numberCallRestrictions = NumberCallsRestriction.objects.filter(link = self.id)
        locationRestrictions = LocationRestriction.objects.filter(link = self.id)

        restriction = []
        if(timeRestrictions.first()):
            restriction = timeRestrictions.first()

        elif(numberCallRestrictions.first()):
            restriction = numberCallRestrictions.first()

        elif(locationRestrictions.first()):
            restriction = locationRestrictions.first()

        if not restriction:
            return None

        return  {
                'restriction': restriction.to_dict(),
                'rNumber': self.real_phone_number.number,
                'vNumber': self.virtual_phone_number.number
                }

class TimeRestriction(models.Model):
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)

    weekdays = models.BooleanField()
    weekends = models.BooleanField()
    link = models.ForeignKey(Link)

    def __str__(self):
     	return "Time %s %s %s %s" % ( self.start_time, self.end_time, self.weekdays, self.weekends)

    def to_dict(self):
        return {
                'type': "Time",
                    'options': {
                        'start': self.start_time,
                        'end': self.end_time,
                        'weekdays': self.weekdays,
                        'weekends': self.weekends
                    }
                }

class LocationRestriction(models.Model):
    country = models.CharField(max_length=50)
    link = models.ForeignKey(Link)

    def __str__(self):
        return "Location %s" % ( self.country )

    def to_dict(self):
        return {
                'type': "Location",
                    'options': {
                        'country': self.country
                    }
                }

class NumberCallsRestriction(models.Model):
    numberCalls = models.IntegerField()
    numberUnits = models.IntegerField()
    unit = models.CharField(max_length=50)
    link = models.ForeignKey(Link)

    def __str__(self):
        return "Number Calls %s %s %s" % ( self.numberCalls, self.numberUnits, self.unit)

    def to_dict(self):
        return {
                'type': "NumberCalls",
                'options': {
                    'numberCalls': self.numberCalls,
                    'numberUnits': self.numberUnits,
                    'unit': self.unit
                    }
                }
