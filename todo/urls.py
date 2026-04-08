from django.urls import path
from . import views

urlpatterns = [
    # add task feature
    path('addTask/',views.addTask,name='addTask'),
    # mark as done feature
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    # mark as undo feature
    path('mark_as_undo/<int:pk>/',views.mark_as_undo,name='mark_as_undo'),
    # edit feature
    path('edit_task/<int:pk>',views.edit_task,name='edit_task'),
    # delete task
    path('delete/<int:pk>/',views.delete_task,name='delete_task')
    ]