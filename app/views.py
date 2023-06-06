from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from datetime import datetime
from .models import *
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from datetime import date
from django.db.models import Q

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect('today')
    else:
        return redirect('login')


def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        return render(request, 'new_task.html', {'form': TaskForm()})


def new_other_task(request):
    if request.method == 'POST':
        form = OtherTaskForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('other_tasks')
    else:
        return render(
            request, 'new_other_task.html', {'form': OtherTaskForm()})


def tasks(request):
    sun_tasks = Task.objects.filter(
        day__icontains="Sunday").filter(done=False)
    mon_tasks = Task.objects.filter(
        day__icontains="Monday").filter(done=False)
    tue_tasks = Task.objects.filter(
        day__icontains="Tuesday").filter(done=False)
    wed_tasks = Task.objects.filter(
        day__icontains="Wednesday").filter(done=False)
    thu_tasks = Task.objects.filter(
        day__icontains="Thursday").filter(done=False)
    fri_tasks = Task.objects.filter(
        day__icontains="Friday").filter(done=False)
    sat_tasks = Task.objects.filter(
        day__icontains="Saturday").filter(done=False)
    return render(
        request,
        'tasks.html',
        {
            'sun_tasks': sun_tasks,
            'mon_tasks': mon_tasks,
            'tue_tasks': tue_tasks,
            'wed_tasks': wed_tasks,
            'thu_tasks': thu_tasks,
            'fri_tasks': fri_tasks,
            'sat_tasks': sat_tasks,
            })


def other_tasks(request):

    date = datetime.now()

    other_tasks = OtherTasks.objects.filter(done=False).order_by('-due')
    overdue_tasks = OtherTasks.objects.filter(
        due__lte=datetime.now()).filter(done=False).order_by('-due').exclude(due=date)
    return render(request, 'other_tasks.html', {
        'other_tasks': other_tasks,
        'overdue_tasks': overdue_tasks})


def new_handover(request):
    if request.method == 'POST':
        form = HandoverForm(request.POST, request.FILES or None)
        if form.is_valid():
            handover = form.save(commit=False)
            handover.user = request.user
            handover.save()
            return redirect('handover')
    else:
        return render(request, 'new_handover.html', {'form': HandoverForm()})


def handover(request):
    unread = Handover.objects.filter(read=False)
    return render(request, 'handover.html', {'unread': unread})


def old_handovers(request):
    read = Handover.objects.filter(read=True)[:10]
    return render(request, 'old_handovers.html', {'read': read})


def mark_read(request, handover_id):
    handover = get_object_or_404(Handover, id=handover_id)
    handover.read = True
    handover.save()
    return redirect('today')


def mark_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.done = True
    task.save()
    return redirect('today')


def mark_other_done(request, othertasks_id):
    task = get_object_or_404(OtherTasks, id=othertasks_id)
    task.done = True
    task.save()
    return redirect('today')


def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('today')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('today')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'change_password.html', {'form': form})


class EditTask(UpdateView):

    model = Task
    template_name = 'edit_task.html'
    fields = [
        'name',
        'day',
        'description',
        ]
    success_url = reverse_lazy('tasks')


class EditOtherTasks(UpdateView):

    model = OtherTasks
    form_class = OtherTaskForm
    template_name = 'edit_other_task.html'
    # fields = [
    #     'name',
    #     'due',
    #     'assigned_to',
    #     'description',
    #     'photo'
    # ]
    success_url = reverse_lazy('other_tasks')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks')


def delete_other(request, othertasks_id):
    task = get_object_or_404(OtherTasks, id=othertasks_id)
    task.delete()
    return redirect('other_tasks')


def calendar(request, year, month):

    cal = HTMLCalendar().formatmonth(year, month)

    now = datetime.now()
    current_year = now.year
    current_month = now.month

    events = Event.objects.filter(date__month=month, date__year=year)

    return render(
        request,
        'calendar.html', {
            'year': year,
            'month': month,
            # 'month_number': month_numnber,
            'cal': cal,
            'current_year': current_year,
            'current_month': current_month,
            'events': events,
            })


def new_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            handover = form.save(commit=False)
            handover.save()
            return redirect('today')
    else:
        return render(request, 'new_event.html', {'form': EventForm()})


class EditEvent(UpdateView):

    model = Event
    form_class = EventForm
    template_name = 'edit_event.html'
    # fields = [
    #     'title',
    #     'date',
    #     'time',
    #     'description',
    #     ]
    success_url = reverse_lazy('today')


def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('other_tasks')


def delete_handover(request, handover_id):
    handover = get_object_or_404(Handover, id=handover_id)
    handover.delete()
    return redirect('old_handovers')


def today(request):
    date = datetime.now()
    day = date.strftime('%A')

    events = Event.objects.filter(date=date).order_by('time')
    dailytasks = Task.objects.filter(day__icontains=day).filter(done=False)
    other_tasks = OtherTasks.objects.filter(done=False).filter(done=False).filter(due=date).order_by('-due')
    overdue_tasks = OtherTasks.objects.filter(
        due__lte=datetime.now()).filter(done=False).order_by('-due').exclude(due=date)

    sun_tasks = Task.objects.filter(
        day__icontains="Sunday").filter(done=False)
    mon_tasks = Task.objects.filter(
        day__icontains="Monday").filter(done=False)
    tue_tasks = Task.objects.filter(
        day__icontains="Tuesday").filter(done=False)
    wed_tasks = Task.objects.filter(
        day__icontains="Wednesday").filter(done=False)
    thu_tasks = Task.objects.filter(
        day__icontains="Thursday").filter(done=False)
    fri_tasks = Task.objects.filter(
        day__icontains="Friday").filter(done=False)
    sat_tasks = Task.objects.filter(
        day__icontains="Saturday").filter(done=False)

    if day == 'Sunday':
        missed_daily = Task.objects.filter(day__icontains='boob')
    elif day == 'Monday':
        missed_daily = Task.objects.filter(day__icontains='Sunday')
    elif day == 'Tuesday':
        missed_daily = Task.objects.filter(
            Q(day__icontains='Sunday') | Q(
                day__icontains='Monday'
            ))
    elif day == 'Wednesday':
        missed_daily = Task.objects.filter(
            Q(day__icontains='Sunday') | Q(
                day__icontains='Monday'
            ) | Q(
                day__icontains='Tuesday'
            ))
    elif day == 'Thursday':
        missed_daily = Task.objects.filter(
            Q(day__icontains='Sunday') | Q(
                day__icontains='Monday'
            ) | Q(
                day__icontains='Tuesday'
            ) | Q(
                day__icontains='Wednesday'
            ))
    elif day == 'Friday':
        missed_daily = Task.objects.filter(
            Q(day__icontains='Sunday') | Q(
                day__icontains='Monday'
            ) | Q(
                day__icontains='Tuesday'
            ) | Q(
                day__icontains='Wednesday'
            ) | Q(
                day__icontains='Thursday'
            ))
    elif day == 'Saturday':
        missed_daily = Task.objects.exclude(
            day__icontains='Saturday'
        )

    lasthandover = Handover.objects.filter(read=False)[:1]

    return render(request, 'today.html', {
        'date': date,
        'day': day,
        'events': events,
        'dailytasks': dailytasks,
        'other_tasks': other_tasks,
        'overdue_tasks': overdue_tasks,
        'missed_daily': missed_daily.filter(done=False),
        'lasthandover': lasthandover
    })


def resettasks(request):
    tasks = Task.objects.filter(done=True)
    for task in tasks:
        task.done = False
        task.save()
    return redirect('tasks')
