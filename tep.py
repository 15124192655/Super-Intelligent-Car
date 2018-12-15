
import urllib2

import json

import time

import datetime

 

APIKEY = '你的APIKey'  

        

        

def http_put():

        file = open("/home/pi/pi/test/dht11/tmp_data.txt")

        temperature= float(file.read())

        CurTime = datetime.datetime.now()

        url='http://api.heclouds.com/devices/你的设备ID/datapoints'

        values={'datastreams':[{"id":"temp","datapoints":[{"at":CurTime.isoformat(),"value":temperature}]}]}

 

        print "the time is: %s" %CurTime.isoformat()

        print "The upload temperature value is: %.3f" %temperature

 

        jdata = json.dumps(values)

        print jdata

        request = urllib2.Request(url, jdata)

        request.add_header('api-key', APIKEY)

        request.get_method = lambda:'POST'

        request = urllib2.urlopen(request)

        return request.read()

 

while True:

        time.sleep(5)

        resp = http_put()

        print "OneNET result:\n %s" %resp

        time.sleep(5)
