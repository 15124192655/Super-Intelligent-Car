#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import logging
import urllib

APIKEY = '你的APIKey'
CYCLETIME= 600 #更新数据的周期
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

    logging.info('sosor is working')
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

def uploadhumtem():
    temperature,humidity=getSensordata()
    logging.info('current sensor result is %s and %s'%(temperature,humidity))
    CurTime = datetime.datetime.now()
    url='http://api.heclouds.com/devices/11302038/datapoints'
    values={'datastreams':[{"id":"hum","datapoints":[{"at":CurTime.isoformat(),"value":humidity}]}]}
    jdata = json.dumps(values)
    logging.debug(jdata)

    request = urllib2.Request(url, jdata)
    request.add_header('api-key', APIKEY)
    request.get_method = lambda:'POST'
    request = urllib2.urlopen(request)
    return request.read()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    while True:
        uploadhumtem()
        time.sleep(CYCLETIME)
    