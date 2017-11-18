# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import TemplateView

from models import Ship
from django.shortcuts import render

Current_Ship = 3

# Create your views here.
def index(request):
    template = 'i3/index.html'
    return render(request,template)


def wc(request):
    template = 'i3/wc.html'
    return render(request,template)


def cockpit(request):
    template = 'i3/cockpit.html'
    return render(request,template)


def engine(request):
    template = 'i3/engine.html'
    return render(request,template)


def status(request):
    ship, created = Ship.objects.get_or_create(pk= Current_Ship)
    ship.update()
    shield = ship.ideal_shield == ship.current_shield
    ship.save()
    template = 'i3/status.html'
    return render(request,template,{'Ship': ship,'Shield':shield})


def cooling_switch(request):
    ship = Ship.objects.get(pk=Current_Ship)
    ship.cooling = not ship.cooling
    ship.save()
    return HttpResponse('BUENO')