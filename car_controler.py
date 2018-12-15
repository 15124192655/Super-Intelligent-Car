
# coding=utf-8

import RPi.GPIO as GPIO

import time

import configparser

 

 

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


 

        GPIO.setmode(GPIO.BOARD)

        GPIO.setwarnings(False)

        GPIO.setup(self.LEFT_FRONT_1, GPIO.OUT)

        GPIO.setup(self.LEFT_FRONT_2, GPIO.OUT)

        GPIO.setup(self.RIGHT_FRONT_1, GPIO.OUT)

        GPIO.setup(self.RIGHT_FRONT_2, GPIO.OUT)
 

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

            print("The input direction is wrong! You can just input: F, B, L, R, BL,BR or S")

 

 

if __name__ == "__main__":

    raspCar = FourWheelDriveCar()

    while(True):

        direction = input("Please input direction: ")

        raspCar.carMove(direction)
