from django.urls import path
from . import views

urlpatterns = [
     path('',views.index),
     path('task_detail/',views.task_detail, name='task_detail'),
     path('update/<int:id>/',views.update,name='update'),
     path('delete/<int:id>/',views.delete,name='delete'),
]
