import urllib
import json
import time
import datetime
import logging

APIKEY = '你的APIKey'  

def http_put():
        file = open("/home/pi/pi/test/dht11/hum_data.txt")
        humidity= float(file.read())
        CurTime = datetime.datetime.now()
        url='http://api.heclouds.com/devices/11302038/datapoints'
        values={'datastreams':[{"id":"hum","datapoints":[{"at":CurTime.isoformat(),"value":humidity}]}]}

        logging.info('the time is: %s' & CurTime.isoformat())
        logging.info('the upload humidity value is: %.3f'%humidity)
 
        jdata = json.dumps(values)
        logging.debug(jdata)

        request = urllib2.Request(url, jdata)
        request.add_header('api-key', APIKEY)
        request.get_method = lambda:'POST'
        request = urllib2.urlopen(request)

        return request.read()

logging.basicConfig(level=logging.INFO)
time.sleep(5)

resp = http_put()
print ("OneNET result:\n %s" %resp)
file.closes
