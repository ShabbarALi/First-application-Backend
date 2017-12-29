# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from TalkingApp.models import User

admin.site.register(User)
#admin.site.register(Choice)