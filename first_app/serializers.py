from rest_framework import serializers
from . models import Asset
from . models import Task
from . models import Worker

class AssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asset
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'#('taskid','name')

class TaskSerializersec(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('taskid','name')

class TaskSerializerAlloc(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('assetid','taskid','workerid','timeOfAllocation','taskToBePerformedBy')

class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = '__all__'
