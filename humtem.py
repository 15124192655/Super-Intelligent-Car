#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import logging
import urllib
'''
This script is used to upload data the sensor gets
With the crontab, you can run it regularly.
'''
# ATTENTION: you also need to replace a url and data structure below.
APIKEY = 'APIKey'
def getSensordata():
    channel=4
    data = []

    GPIO.setmode(GPIO.BCM)
    time.sleep(1)

    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(0.02)

    GPIO.output(channel, GPIO.HIGH)
    GPIO.setup(channel, GPIO.IN)


    while GPIO.input(channel) == GPIO.LOW:
        pass
    while GPIO.input(channel) == GPIO.HIGH:
        pass

    j = 0
    while j < 40:
        k = 0
        while GPIO.input(channel) == GPIO.LOW:
            pass

        while GPIO.input(channel) == GPIO.HIGH:
            k += 1
            if k > 100:
                break

        if k < 8:
            data.append(0)
        else:
            data.append(1)
        j += 1

    logging.info('sonsor is working well')
    logging.info('read data: {data}')

    # converting data
    humidity_bit = data[0:8]
    humidity_point_bit = data[8:16]
    temperature_bit = data[16:24]
    temperature_point_bit = data[24:32]
    check_bit = data[32:40]

    humidity = 0
    humidity_point = 0
    temperature = 0
    temperature_point = 0
    check = 0

    for i in range(8):
        humidity += humidity_bit[i] * 2 ** (7-i)
        humidity_point += humidity_point_bit[i] * 2 ** (7-i)
        temperature += temperature_bit[i] * 2 ** (7-i)
        temperature_point += temperature_point_bit[i] * 2 ** (7-i)
        check += check_bit[i] * 2 ** (7-i)

    tmp = humidity + humidity_point + temperature + temperature_point

    if check != tmp:
        logging.error('error when checking data, dont trust it. is there something wrong with sensor?')
    
    GPIO.cleanup()
    return temperature,humidity

def postdata(url,data):
    curtime=datetime.datetime.now()
    logging.debug(jdata)

    request = urllib2.Request(url, json.dumps(data))
    request.add_header('api-key', APIKEY)
    request.get_method = lambda:'POST'
    request = urllib2.urlopen(request)
    return request.read()
    

def uploadhumtem():
    temperature,humidity=getSensordata()
    logging.info('current sensor result is {temperature} and {humidity}')
    CurTime = datetime.datetime.now()
    # put the uploading url and data here
    postdata('http://api.heclouds.com/devices/11302038/datapoints',{'datastreams':[{"id":"hum","datapoints":[{"at":CurTime.isoformat(),"value":humidity}]}]})
    # end

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    uploadhumtem()
    
