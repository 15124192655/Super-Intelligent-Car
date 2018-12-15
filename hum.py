
import urllib2

import json

import time

import datetime

 

APIKEY = '你的APIKey'  

        

        

def http_put():

        file = open("/home/pi/pi/test/dht11/hum_data.txt")

        humidity= float(file.read())

        CurTime = datetime.datetime.now()

        url='http://api.heclouds.com/devices/11302038/datapoints'

        values={'datastreams':[{"id":"hum","datapoints":[{"at":CurTime.isoformat(),"value":humidity}]}]}

 

        print "the time is: %s" %CurTime.isoformat()

        print "The upload humidity value is: %.3f" %humidity

 

        jdata = json.dumps(values)

        print jdata

        request = urllib2.Request(url, jdata)

        request.add_header('api-key', APIKEY)

        request.get_method = lambda:'POST'

        request = urllib2.urlopen(request)

        return request.read()

 

 

time.sleep(5)

resp = http_put()

print "OneNET result:\n %s" %resp

file.closes
