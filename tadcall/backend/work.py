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

def get_link(req):
    user_id = req.GET['id']
    links = Link.objects.filter(user = user_id)
    content = map(links, lambda x: x.to_json())
    return make_response(content)


def make_response(content):
    return HttpResponse(json.dumps(content), CONTENT_TYPE)
