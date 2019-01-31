# coding=utf-8
import time
import configparser
import asyncio
import logging


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

        self.queue_motor=[]
 

    def reset(self):
        pass

    def __forword(self):
        self.reset()

    def __backword(self):
        self.reset()

    def __turnLeft(self):
        '''
        To turn left, the LEFT_FRONT wheel will move backword
        All other wheels move forword
        '''
        self.reset()

    def __turnRight(self):
        '''
        To turn right, the RIGHT_FRONT wheel move backword
        All other wheels move forword

        '''
        self.reset()

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
        TODO: express action series like this,'<id>:<abstract angle>,' one by one.
        '''
        #ACTION={'seize':'i:10,l:20'}
        #series=ACTION['id'].split(',')
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
            #print("The input direction is wrong! You can just input: F, B, L, R, BL,BR or S")
            return False,"The input direction is wrong! You can only input: F,B,L,R,BL,BR or S";
        return True,'ok'

if __name__ == "__main__":
    raspCar = FourWheelDriveCar()
    while(True):
        direction = input("Please input direction: ")
        raspCar.carMove(direction)
