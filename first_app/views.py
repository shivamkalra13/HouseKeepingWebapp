from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Asset
from . models import Task
from . models import Worker
from . serializers import AssetSerializer
from . serializers import TaskSerializer
from . serializers import TaskSerializersec
from . serializers import WorkerSerializer
from . serializers import TaskSerializerAlloc
import json

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

class AssetList(APIView):

    def get(self, request):
        assets = Asset.objects.all()
        serializer = AssetSerializer(assets, many =True)
        return Response(serializer.data)

class AssetAdd(APIView):
    def get(self, request):
        assets = Asset.objects.all()
        serializer = AssetSerializer(assets, many =True)
        return Response(serializer.data)
    def post(self, request):
         serializer = AssetSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskAdd(APIView):
    def get(self, request):
        assets = Task.objects.all()
        serializer = TaskSerializer(assets, many =True)
        return Response(serializer.data)
    def post(self, request):
         serializer = TaskSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkerAdd(APIView):
    def get(self, request):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many =True)
        return Response(serializer.data)
    def post(self, request):
         serializer = WorkerSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskAlloc(APIView):
    def get(self, request):
        assets = Task.objects.all()
        serializer = TaskSerializerAlloc(assets, many =True)
        return Response(serializer.data)
    def post(self, request):
         serializer = TaskSerializerAlloc(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskForWorker(APIView):

    def get_tasks(self, wid):
        try:
            return Task.objects.filter(workerid = Worker.objects.get(workerid = wid)).values()
        except:
             raise Http404

    def get(self,request,wid):
        #wid = request.GET['wid']
        tasks = self.get_tasks(wid)
        #tasks = Task.objects.all()
        #tasks = self.get_tasks(wid)
        serializer = TaskSerializersec(tasks, many =True)
        return Response(serializer.data)
