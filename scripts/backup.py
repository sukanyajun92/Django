__author__ = 'suksubra'
#!/usr/local/bin/python3.5

#script.py
import csv
import sqlite3
import traceback
from datetime import datetime

conn = sqlite3.connect("example.db")
curs = conn.cursor()
curs.execute("drop table if exists SYS;")
try:
    curs.execute("CREATE TABLE SYS (CHASSISNAME TEXT, TIME TEXT, AVERAGE_PACKET_SIZE TEXT, CPU_0_5MIN_AVG_SESSMGR_CPUS TEXT, EDR_SEC TEXT,SESSMGR_ACTIVE_CARDS TEXT, THROUGHPUT_KPPS TEXT, THROUGHPUT_MBPS TEXT, TOTAL_CALLS_CONNECTED_SEC TEXT, TOTAL_CALLS_DISCONNECTED_SEC TEXT, TOTAL_SUBSCRIBERS TEXT, UDR_SEC TEXT)")
    print ("Successfully created!!!")
except:
    print ("Unable to create database")

with open("/Users/suksubra/Documents/OfficeFiles/CSV/sysengine.csv") as f:
    content = f.read()

lines = content.split("\n")
count =  len(lines)

for i in range(1,count-1):
    line = lines[i].split(",")
    command = "insert into sys values('vzwperf51','" + line[0] + "'"
    for j in range (1,len(line)):
        try:
            command +=",'" + line[j] + "'"
        except:
            print("Error appending")
    command += ");"
    try:
        curs.execute(command)
    except:
        traceback.print_exc()
        print("Error inserting")

try:
    for row in curs.execute("select * from sys"):
        print(row)
except:
    print("Error in select")

conn.commit()


#views.py
__author__ = 'suksubra'

from .models import chassisInfo
from rest_framework import status
from .serializers import chassisSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def chassis_list(request, format=None):
    """
    List all code chassiss, or create a new chassis.
    """
    if request.method == 'GET':
        chassiss = chassisInfo.objects.all()
        serializer = chassisSerializer(chassiss, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = chassisSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

##Version2:
class chassisList(generics.ListCreateAPIView):
    queryset = chassisInfo.objects.all()
    serializer_class = chassisSerializer


#urls.py
from django.conf.urls import include, url
from django.contrib import admin
from application.views import chassisList

urlpatterns = [
    url(r'^application/$', chassisList.as_view()),
    url(r'^admin/', include(admin.site.urls)),
]

#models.py
__author__ = 'suksubra'
from django.db import models

class chassisInfo(models.Model):
    TIME = models.CharField(max_length=200)
    AVERAGE_PACKET_SIZE = models.CharField(max_length=200)
    CPU_0_5MIN_AVG_SESSMGR_CPUS = models.CharField(max_length=200)
    EDR_SEC = models.CharField(max_length=200)
    SESSMGR_ACTIVE_CARDS = models.CharField(max_length=200)
    THROUGHPUT_KPPS = models.CharField(max_length=200)
    THROUGHPUT_MBPS = models.CharField(max_length=200)
    TOTAL_CALLS_CONNECTED_SEC = models.CharField(max_length=200)
    TOTAL_CALLS_DISCONNECTED_SEC = models.CharField(max_length=200)
    TOTAL_SUBSCRIBERS = models.CharField(max_length=200)
    UDR_SEC = models.CharField(max_length=200)

    def __str__(self):
        return self.TIME




