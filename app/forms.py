from django.forms import ModelForm
from django import forms
from .models import Task, Handover, OtherTasks, Event


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_time = 'time'


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            # 'due',
            'day',
            # 'repeat',
            # 'assigned_to',
            'description',
            ]


class OtherTaskForm(ModelForm):
    class Meta:
        model = OtherTasks
        fields = [
            'name',
            'due',
            'assigned_to',
            'description',
            'photo'
            ]
        widgets = {
            'due': DateInput(),
        }


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'date',
            'time',
            'description'
        ]
        widgets = {
            'date': DateInput(),
            'time': TimeInput(attrs={'type': 'time'}),
        }


class HandoverForm(ModelForm):
    class Meta:
        model = Handover
        fields = [
            'message',
            'photo',
            'photo2',
            'photo3'
        ]
