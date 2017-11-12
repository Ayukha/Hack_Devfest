# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views import generic

# Create your views here.

from .models import timezone

class IndexView(generic.ListView):
	tmeplate_name = "######"
	context_object_name = #####



class DetailView(generic.DetailView):
	model = 
	template_name = "######"


class ResultView(generic.DetailView):
	model =  ######
	tmeplate_name = #####


def Vote(request, ########)


