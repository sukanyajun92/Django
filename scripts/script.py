__author__ = 'suksubra'
#!/usr/local/bin/python3.5

import csv
import sqlite3
import traceback
from application.models import chassisInfo
import os,django,sys

sys.path.append("/root/poll/projects/sysengine/application")
os.environ["DJANGO_SETTINGS_MODULE"] = "sysengine.settings"
django.setup()

with open('sysengine.csv') as f:
    reader = csv.reader(f, delimiter=',')
    header = next(reader)
    print("header  = " )
    print(header)
    i = 0
    for row in reader:
        try:
            print (row[0])
            chassis = chassisInfo()
            chassis.TIME = row[0]
            chassis.AVERAGE_PACKET_SIZE = row[1]
            chassis.CPU_0_5MIN_AVG_SESSMGR_CPUS = row[2]
            chassis.EDR_SEC = row[3]
            chassis.SESSMGR_ACTIVE_CARDS = row[4]
            chassis.THROUGHPUT_KPPS = row[5]
            chassis.THROUGHPUT_MBPS = row[6]
            chassis.TOTAL_CALLS_CONNECTED_SEC = row[7]
            chassis.TOTAL_CALLS_DISCONNECTED_SEC = row[8]
            chassis.TOTAL_SUBSCRIBERS = row[9]
            chassis.UDR_SEC = row[10]
            chassis.save()
        except:
            traceback.print_exc()
            print("Error saving..")