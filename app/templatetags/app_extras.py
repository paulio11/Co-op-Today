from django import template
from datetime import datetime, timedelta
from ..models import *
from datetime import date
from datetime import datetime


register = template.Library()


@register.simple_tag
def other_notdone():
    notdone = OtherTasks.objects.filter(done=False)
    return notdone.count()


@register.simple_tag
def daily_notdone():
    if date.today().weekday() == 6:
        notdone = Task.objects.filter(done=False, day__icontains="Sunday")
    elif date.today().weekday() == 0:
        notdone = Task.objects.filter(done=False, day__icontains="Monday")
    elif date.today().weekday() == 1:
        notdone = Task.objects.filter(done=False, day__icontains="Tuesday")
    elif date.today().weekday() == 2:
        notdone = Task.objects.filter(done=False, day__icontains="Wednesday")
    elif date.today().weekday() == 3:
        notdone = Task.objects.filter(done=False, day__icontains="Thursday")
    elif date.today().weekday() == 4:
        notdone = Task.objects.filter(done=False, day__icontains="Friday")
    elif date.today().weekday() == 5:
        notdone = Task.objects.filter(done=False, day__icontains="Saturday")
    return notdone.count()


@register.simple_tag
def nowyear():
    now = datetime.now()
    year = now.year
    return year


@register.simple_tag
def nowmonth():
    now = datetime.now()
    month = now.month
    return month


@register.simple_tag
def monthevents():
    now = datetime.now()
    month = now.month
    year = now.year
    events = Event.objects.filter(date__month=month, date__year=year)
    return events.count()