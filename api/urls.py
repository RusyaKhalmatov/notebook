from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name = 'apiOverview'),
    path('/all-topics', views.taskList, name='taskList')
]