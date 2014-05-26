'''
Created on 2014-5-18

@author: Administrator
'''
import json
import time
import datetime
from django.http import HttpResponse
from django.http import Http404

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics

from django.shortcuts import render

from learn.models import History, Remind
from learn.serializers import HistorySerializer, RemindSerializer

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'history-list': reverse('history-list', request=request, format=format),
        'history-detail': reverse('history-detail', request=request, format=format),
        
    })
@csrf_exempt        
def login(request):
    userName = request.session.get('ln_user', None)
    print 'userName=[%s] in login' % userName
    if userName:
        responseData = {'userName': userName}
        return render(request, 'mainForm', responseData)

    if request.method == 'GET':
        return render(request, 'loginForm')
    print "POST for login verification..."
    userName = request.POST.get('userName', 'learn')
    #password = request.POST.get('password')

    print 'userName=[%s]' % (userName)

    responseData = {'userName': userName}
    request.session['ln_user'] = userName
    user_id = 0
    request.session['ln_userid'] = user_id
    return render(request, 'mainForm', responseData)
@csrf_exempt
def logout(request):
    if request.session.get('ln_user', None):
        try:
            del request.session['ln_user']
            del request.session['ln_userid']
            print 'logout done !'
        except Exception, e:
            print '%s' % e

    return render(request, 'loginForm')

class HistoryList(generics.ListCreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class HistoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    
class RemindsList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Remind.objects.filter(id=0)
    #serializer_class = RemindSerializer
    def get(self, request, format=None):
        remind = Remind.objects.all()
        serializer = RemindSerializer(remind, many=True)
        return Response(serializer.data)
    def post(self, request,his, format=None):
        serializer = RemindSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RemindsListByHis(RemindsList):    
    def get(self, request, his,format=None):
        remind = Remind.objects.filter(history=his)
        serializer = RemindSerializer(remind, many=True)
        return Response(serializer.data)
  
class RemindsDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    queryset = Remind.objects.filter(id=0)
    def get_object(self, his,pk):
        try:
            return Remind.objects.get(history=his,pk=pk)
        except Remind.DoesNotExist:
            raise Http404

    def get(self, request,his, pk, format=None):
        remind = self.get_object(his,pk)
        serializer = RemindSerializer(remind)
        return Response(serializer.data)

    def put(self, request,his, pk, format=None):
        remind = self.get_object(his,pk)
        serializer = RemindSerializer(remind, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,his, pk, format=None):
        remind = self.get_object(his,pk)
        remind.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
class RemindDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Remind.objects.all()
    serializer_class = RemindSerializer   