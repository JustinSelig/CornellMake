from django.shortcuts import render
import datetime
from models import Event

def home(request):
	day = 6 #replace from demo: datetime.datetime.now().day
	month = datetime.datetime.now().month
	year = datetime.datetime.now().year
	event = Event.objects.get(day=day, month=month, year=year)
	context = {}
	context['event'] = event
	return render(request, 'index.html', context)