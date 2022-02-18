from django.contrib import admin

from .models import Command, Device

admin.site.register(Command)
admin.site.register(Device)
admin.site.site_header = "MONITOR ENGINE"
