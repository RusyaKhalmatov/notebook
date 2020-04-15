from rest_framework import serializers
from learning_logs.models import Topic

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Topic
        fields = '__all__'

