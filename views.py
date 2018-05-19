from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.template.loader import get_template
from django.utils import timezone
from django.http import HttpResponse, Http404
from .models import  Event, Sport, Team, Channel, Game, Venue
import datetime

# Create your views here.

class AllListView(generic.ListView):
    model = Game
    template_name = 'fbwc/index.html'    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()

        result_team = Team.objects.values('group').distinct().order_by('group')
        context['grl'] = result_team

        team_list = Team.objects.order_by('name')
        context['teaml'] = team_list

        result_date = Game.objects.values('date').distinct().order_by('date')
        context['datelist'] = result_date

        return context
