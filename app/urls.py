from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new_task/', views.new_task, name='new_task'),
    path('new_other_task/', views.new_other_task, name='new_other_task'),
    path('tasks/', views.tasks, name='tasks'),
    path('other_tasks/', views.other_tasks, name='other_tasks'),
    path('handover/', views.handover, name='handover'),
    path('old_handovers/', views.old_handovers, name='old_handovers'),
    path('new_handover/', views.new_handover, name='new_handover'),
    path('<handover_id>/read', views.mark_read, name='mark_read'),
    path('<task_id>/done', views.mark_done, name='mark_done'),
    path('<othertasks_id>/otherdone', views.mark_other_done, name='mark_other_done'),
    path('login/', views.login_view, name='login'),
    path('password/', views.change_password, name='password'),
    path('edit/<int:pk>', views.EditTask.as_view(), name='edit_task'),
    path('editother/<int:pk>', views.EditOtherTasks.as_view(), name='edit_other'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('deleteother/<othertasks_id>', views.delete_other, name='delete_other'),
    path('calendar/<int:year>/<int:month>/', views.calendar, name='calendar'),
    path('new_event/', views.new_event, name='new_event'),
    path('edit_event/<int:pk>', views.EditEvent.as_view(), name='edit_event'),
    path('delete_event/<event_id>', views.delete_event, name='del_event'),
    path('today/', views.today, name='today'),
    path('reset/', views.resettasks, name='reset'),
    path('deletehandover/<handover_id>', views.delete_handover, name='delete_handover'),
]
