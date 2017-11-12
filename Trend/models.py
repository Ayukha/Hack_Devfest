# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Doctors(models.Model):
	user = models.onetooneField(User, on_delete=models.CASCADE,null=True)
	degree = models.IntegerField()
	City = models.CharField(maxlength=40)
	State = models.CharField(maxlength=40)
	Country = models.CharField(maxlength=40)




class Disease(models.Model):
	Name = models.CharField(maxlength=40,blank=False)
	Description = models.TextField(null=False,blank=False)
	Precaution = models.TextField(null=False,blank=False)
	Symptoms = models.TextField(null=False,blank=False)


	def __str__(self):
        return unicode(self.Name)



class Choice(models.Model):
	disease_name =models.ForeignKey(Disease, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)



    def __str__(self):
        return unicode(self.choice_text)


