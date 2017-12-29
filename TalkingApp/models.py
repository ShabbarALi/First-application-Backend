# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
# from django.utils import timezone
from datetime import datetime
from django.core.validators import RegexValidator

class User(models.Model):
    Quick_Id = models.CharField(max_length=30,primary_key=True)
    Name = models.CharField(max_length=40, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    # Phone=models.PhoneNumberField(unique=True,blank=True,null=True)
    # email = models.EmailField(blank=True, verbose_name='e-mail')
    def __repr__(self):
        return (self.Name,self.Phone)
        # return u'%s %s' % (self.Quick_ID, self.Name,self.Phone)
    def __str__(self):
        return(self.Quick_Id)

class UserLogging(models.Model):
    Quick_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    # date = models.DateTimeField(default=datetime.now, blank=True)
    last_Logging_Time = models.DateTimeField(editable=False,blank=True)
    def __init__(self, *args, **kwargs):
        super(UserLogging, self).__init__(*args, **kwargs)
        self.last_Logging_Time = datetime.now()
    def __repr__(self):
    	return (self.last_Logging_Time)
    def __str__(self):
    	return str(self.Quick_Id)
    	   			   	

                
