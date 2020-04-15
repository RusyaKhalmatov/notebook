from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from learning_logs.models import Topic
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list',
        'Detail View':'.task/detail/<str:pl>/',
        'Create':'/task-create',
        'Delete':'task-delete/<str:pk>/',
        'Update': 'task-update/<str:pk>/'
    }

    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    topics = Topic.objects.all()
    text = {}
    for topic in topics:
        entries = topic.entry_set.order_by("-date_added")
        text = {topic}

    serializer = TaskSerializer(text, many=True)
    return Response(serializer.data)