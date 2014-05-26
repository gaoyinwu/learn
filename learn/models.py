'''
Created on 2014-5-18

@author: Administrator
'''
from django.db import models

# Create your models here.
class History(models.Model):
    id = models.AutoField('id', primary_key=True)
    name = models.CharField(db_column='ln_name',max_length=64)
    question= models.TextField(db_column='ln_question')
    answer = models.TextField(db_column='ln_answer',default='')
    createtime = models.DateField(db_column='ln_createtime',auto_now_add=True)
    userid = models.IntegerField(db_column='ln_userid',default=0)
    class Meta:
        db_table = "ln_history"
class Remind(models.Model):
    id = models.AutoField('id', primary_key=True)
    history = models.IntegerField(db_column='ln_history_id')
    date= models.DateField(db_column='ln_date')
    status = models.CharField(db_column='ln_status',default='initial',max_length=20)
    confirmtime = models.DateField(db_column='ln_confirmdate',default=None)
    userid = models.IntegerField(db_column='ln_userid',default=0)
    class Meta:
        db_table = "ln_remind"
