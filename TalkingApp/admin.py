# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from datetime import datetime

# Register your models here.

from TalkingApp.models import UserLogging,User
class UserLoggingAdmin(admin.ModelAdmin):
    readonly_fields = ('last_Logging_Time',)
    def save_model(self, request, obj, form, change):
        	# if obj.Quick_Id and 'Quick_Id' in form.changed_data:
        	# millis = int(round(time.time() * 1000))
        obj.last_Logging_Time = datetime.now()
        obj.save()

admin.site.register(User)
admin.site.register(UserLogging,UserLoggingAdmin)

