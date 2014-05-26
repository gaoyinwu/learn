'''
Created on 2014-5-24

@author: Administrator
'''
from django.forms import widgets
from rest_framework import serializers
from learn.models import History,Remind


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('id', 'name', 'question', 'answer', 'createtime', 'userid')
class RemindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remind
        fields = ('id', 'history', 'date', 'status', 'confirmtime', 'userid')
