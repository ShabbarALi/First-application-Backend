# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Loggin(models.Model):
    Quick_Id = models.IntegerField(default=0)
    # date = models.DateTimeField(default=datetime.now, blank=True)
    date_generated = models.DateTimeField(default=timezone.now, editable=False,blank=True)
    def __repr__(self):
    	return (self.date_generated)
    def __str__(self):
    	return str(self.Quick_Id)
    	   			   	

#     question = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

#     # HERE 
#     def __str__(self):
#         return self.question


# class Choice(models.Model):
#     Question = models.ForeignKey(Question,on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     # AND HERE
#     def __str__(self):
#     	return self.choice_text

