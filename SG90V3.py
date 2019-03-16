#!/usr/bin/env python


import RPi.GPIO as GPIO
import time
import signal
import atexit

atexit.register(GPIO.cleanup) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT, initial=False)

GPIO.setup(27, GPIO.OUT, initial=False)
p1= GPIO.PWM(17,50) #50HZ

p2= GPIO.PWM(27,50) #50HZ
p1.start(0)
p2.start(0)
time.sleep(2)

while(True):
  for i in range(0,181,10):
    p1.ChangeDutyCycle(2.5 + 10 * i / 180) #设置转动角度
    time.sleep(0.02)                      #等该20ms周期结束
    p1.ChangeDutyCycle(0)                  #归零信号
    time.sleep(0.2)

  for i in range(181,0,-10):
    p2.ChangeDutyCycle(2.5 + 10 * i / 180)
    time.sleep(0.02)
    p2.ChangeDutyCycle(0)
    time.sleep(0.2)

