from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from backend.models import *
from backend.apidaze import *

import pdb
import json

CONTENT_TYPE = 'application/json'

def get_user(req):
    name = req.GET['name']
    user = User.objects.filter(name = name).first()
    content = {'user_id' : user.id}
    return make_response(content)

def get_links(req):
    user_id = req.GET['user_id']
    links = Link.objects.filter(user = user_id)
    content = map(lambda x: x.to_dict(), links)

    return make_response(content)

@csrf_exempt
def add_real_phone_number(req):
    real_phone_number = req.GET['real_phone_number']
    user_id = req.GET['user_id']
    user = User.objects.filter(id = user_id).first()
    rpn = RealPhoneNumber()
    rpn.number = real_phone_number
    rpn.user = user
    rpn.save()
    return HttpResponse()


def delete_real_phone_number(req):
    real_phone_number = req.GET['real_phone_number'].strip()
    number = RealPhoneNumber.objects.filter(number = real_phone_number).first()

    if number:
	    number.delete()
	    return HttpResponse("Deleted")
    return HttpResponse("Not found")

def add_link(req):
    user_id=req.GET['user_id']
    real_phone_number=req.GET['real_phone_number']

    # make API call to get a virtual phone
    virtual_phone_number = VirtualPhoneNumber.objects.first()

    # create link
    link = Link()
    link.user = User.objects.filter(id=user_id).first()
    link.virtual_phone_number = virtual_phone_number
    link.real_phone_number = RealPhoneNumber.objects.filter(number=real_phone_number).first()
    link.save()

    # devolver link
    return make_response(link.to_dict())

@csrf_exempt
def add_link_with_restrictions(req):
    body = json.loads(req.body)
    user_id=req.GET['user_id']

    rest_type = body['type']
    virtual_number_s = body['vNumber']
    real_number_s = body['rNumber']

    virtual_number = VirtualPhoneNumber.objects.filter(number=virtual_number_s).first()
    real_number = RealPhoneNumber.objects.filter(number=real_number_s).first()

    if not virtual_number or not real_number:
	return make_response("Non existing number")

    link = Link()
    link.virtual_phone_number = virtual_number
    link.real_phone_number = real_number
    link.user = User.objects.filter(id=user_id).first()
    link.save()

    if rest_type == 'Time':
      start = body['options']['start']
      end = body['options']['end']
      weekdays = body['options']['weekdays']
      weekends = body['options']['weekends']

      restriction = TimeRestriction()
      restriction.start_time = start
      restriction.end_time = end
      restriction.weekdays = weekdays
      restriction.weekends = weekends
      restriction.link = link
      restriction.save()

    elif rest_type == 'Location':
      country = body['options']['country']

      restriction = LocationRestriction()
      restriction.country = country
      restriction.link = link
      restriction.save()

    else:
      numberCalls = body['options']['numberCalls']
      numberUnits = body['options']['numberUnits']
      units = body['options']['unit']

      restriction = NumberCallsRestriction()
      restriction.numberCalls = numberCalls
      restriction.numberUnits = numberUnits
      restriction.unit = units
      restriction.link = link
      restriction.save()

    return make_response("ok")

def get_real_phone_numbers(req):
    user_id = req.GET['user_id']
    rtns = RealPhoneNumber.objects.filter(user = user_id)
    content = map(lambda x: x.to_dict(), rtns)
    return make_response(content)

def get_virtual_phone_numbers(req):
    user_id = req.GET['user_id']
    rtns = VirtualPhoneNumber.objects.filter(user = user_id)
    content = map(lambda x: x.to_dict(), rtns)
    return make_response(content)

def answer(req):
    dialed_phone_number=req.GET['destination_number']
    virtual_phone_number = VirtualPhoneNumber.objects.filter(number=dialed_phone_number).first()

    print dialed_phone_number
    if(virtual_phone_number):
	    print "ACCEPT"
	    return make_xml_response(dial('00351964817388'))
    else:
	    print "REJECT"
	    return make_xml_response(hangup())

def make_response(content):
    return HttpResponse(json.dumps(content), CONTENT_TYPE)

def make_xml_response(content):
    res = HttpResponse(content, 'text/xml; charset=us-ascii')

    return res
