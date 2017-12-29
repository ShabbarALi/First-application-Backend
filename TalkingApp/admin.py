# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


# Register your models here.

from TalkingApp.models import Loggin
class LogginAdmin(admin.ModelAdmin):

    readonly_fields = ('date_generated',)

admin.site.register(Loggin,LogginAdmin)


