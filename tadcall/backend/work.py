from django.http import HttpResponse

from backend.models import *
import pdb
import json

CONTENT_TYPE = 'application/json'

def get_user(req):
    name = req.GET['name']
    user = User.objects.filter(name = name).first()
    content = {'id' : user.id}
    return make_response(content)

def get_links(req):
    user_id = req.GET['id']
    links = Link.objects.filter(user = user_id)
    content = map(lambda x: x.to_dict(), links)
    return make_response(content)

def add_real_phone_number(req):
    real_phone_number = req.GET['real_phone_number']
    user_id = req.GET['user_id']
    user = User.objects.filter(id = user_id).first()
    rpn = RealPhoneNumber()
    rpn.number = real_phone_number
    rpn.user = user
    rpn.save()
    return HttpResponse()

def add_link(req):
    # make API call to get a virtual phone

    return 0


def make_response(content):
    return HttpResponse(json.dumps(content), CONTENT_TYPE)
