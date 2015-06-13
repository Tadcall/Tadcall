from django.contrib import admin

from backend.models import *

# Register your models here.

admin.site.register(User)
admin.site.register(RealPhoneNumber)
admin.site.register(VirtualPhoneNumber)
admin.site.register(Link)
