# coding=utf-8

import RPi.GPIO as GPIO
import time
import configparser
import signal
import atexit
import asyncio


class FourWheelDriveCar():
    # Define the number of all the GPIO that will used for the 4wd car
    def __init__(self):
        '''
        1. Read pin number from configure file
        2. Init all GPIO configureation

        '''
        config = configparser.ConfigParser()
        config.read("config.ini")
        self.LEFT_FRONT_1 = config.getint("car", "LEFT_FRONT_1")
        self.LEFT_FRONT_2 = config.getint("car", "LEFT_FRONT_2")
        self.RIGHT_FRONT_1 = config.getint("car", "RIGHT_FRONT_1")
        self.RIGHT_FRONT_2 = config.getint("car", "RIGHT_FRONT_2")
        
        self.CAM_P1=11
        self.CAM_P2=13

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        GPIO.setup(self.LEFT_FRONT_1, GPIO.OUT)
        GPIO.setup(self.LEFT_FRONT_2, GPIO.OUT)
        GPIO.setup(self.RIGHT_FRONT_1, GPIO.OUT)
        GPIO.setup(self.RIGHT_FRONT_2, GPIO.OUT)
        GPIO.setup(self.CAM_P1,GPIO.OUT,initial=False)
        GPIO.setup(self.CAM_P2,GPIO.OUT,initial=False)

        self.camp1=GPIO.PWM(self.CAM_P1,50)
        self.camp2=GPIO.PWM(self.CAM_P2,50)
 

    def reset(self):
        # Rest all the GPIO as LOW
        GPIO.output(self.LEFT_FRONT_1, GPIO.LOW)
        GPIO.output(self.LEFT_FRONT_2, GPIO.LOW)
        GPIO.output(self.RIGHT_FRONT_1, GPIO.LOW)
        GPIO.output(self.RIGHT_FRONT_2, GPIO.LOW)

    def __forword(self):
        self.reset()

        GPIO.output(self.LEFT_FRONT_1, GPIO.HIGH)
        GPIO.output(self.LEFT_FRONT_2, GPIO.LOW)
        GPIO.output(self.RIGHT_FRONT_1, GPIO.HIGH)
        GPIO.output(self.RIGHT_FRONT_2, GPIO.LOW)

    def __backword(self):
        self.reset()

        GPIO.output(self.LEFT_FRONT_2, GPIO.HIGH)
        GPIO.output(self.LEFT_FRONT_1, GPIO.LOW)
        GPIO.output(self.RIGHT_FRONT_2, GPIO.HIGH)
        GPIO.output(self.RIGHT_FRONT_1, GPIO.LOW)

    def __turnLeft(self):
        '''
        To turn left, the LEFT_FRONT wheel will move backword
        All other wheels move forword
        '''
        self.reset()

        GPIO.output(self.LEFT_FRONT_2, GPIO.HIGH)
        GPIO.output(self.LEFT_FRONT_1, GPIO.LOW)
        GPIO.output(self.RIGHT_FRONT_1, GPIO.HIGH)
        GPIO.output(self.RIGHT_FRONT_2, GPIO.LOW)

    def __turnRight(self):
        '''
        To turn right, the RIGHT_FRONT wheel move backword
        All other wheels move forword

        '''
        self.reset()

        GPIO.output(self.LEFT_FRONT_1, GPIO.HIGH)
        GPIO.output(self.LEFT_FRONT_2, GPIO.LOW)
        GPIO.output(self.RIGHT_FRONT_2, GPIO.HIGH)
        GPIO.output(self.RIGHT_FRONT_1, GPIO.LOW)

    def __stop(self):
        self.reset()

    async def setmotor(self,id,angle):
        '''
        TODO: this function is used to control possible motors.
        angle is supposed to be ABSTRACT.
        '''
        logging.info("set %s to %s" % (id,angle))
        await asyncio.sleep(1) #fake action

    async def doaction(self,cmd):
        '''
        'cmd' express action series like this,'<id>:<abstract angle>,' one by one.
        '''
        series=cmd.split(',')
        for i in series:
            temp=i.split(':')
            await self.setmotor(temp[0],temp[1])
 

    def carMove(self, direction):
        '''
        Car move according to the input paramter - direction
        '''
        if direction == 'F':
            self.__forword()
        elif direction == 'B':
            self.__backword()
        elif direction == 'L':
            self.__turnLeft()
        elif direction == 'R':
            self.__turnRight()
        elif direction == 'BL':
            self.__backLeft()
        elif direction == 'BR':
            self.__backRight()
        elif direction == 'S':
            self.__stop()
        else:
            return false,"The input direction is wrong! You can only input: F,B,L,R,BL,BR or S";
        return True,'ok'
    async def cammove(self,axis,rot):
        if(axis=="p1"):
            temp=self.camp1
        elif(axis=="p2"):
            temp=self.camp2
        
        temp.ChangeDutyCycle(2.5+10*int(rot)/180)
        await asyncio.sleep(0.02)
        temp.ChangeDutyCycle(0)
        await asyncio.sleep(0.2)

        


if __name__ == "__main__":
    raspCar = FourWheelDriveCar()
    while(True):
        direction = input("Please input direction: ")
        raspCar.carMove(direction)

