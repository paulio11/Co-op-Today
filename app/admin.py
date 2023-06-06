from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Handover)


@admin.action(description='Reset daily tasks to done = false')
def reset_task(modeladmin, request, queryset):
    queryset.update(done=False)


class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'day', 'done']
    ordering = ['day']
    actions = [reset_task]


class OtherTaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'done']
    actions = [reset_task]


admin.site.register(Task, TaskAdmin)
admin.site.register(OtherTasks, OtherTaskAdmin)
admin.site.register(Event)
