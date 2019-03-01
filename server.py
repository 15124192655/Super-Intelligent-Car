# --coding:utf-8--
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import socket
import urllib
from car_controller import FourWheelDriveCar
import asyncio
import websockets
from wsserver import WsServer
import wsserver
import json
import logging
carControler = FourWheelDriveCar()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    wss=WsServer('9090',True)
    async def bind_move(data,ws):
        r1,r2=carControler.carMove(data['direction'])
    
    async def bind_motor(data,ws):
        await carControler.setmotor(data['id'],data['angle'])
        logging.info('setmotor %s %s'%(data['id'],data['angle']))

    async def bind_action(data,ws):
        await carControler.doaction(data['cmd'])
    
    # heartbeat signal
    # used to check if the connection and server is under good condition.
    async def bind_chika(data,ws):
        # chika kawai!
        await wsserver.Data("chika").add('msg','heartbeat, server is good. chika kawai').send(ws)


    # register handlers here
    wss.hand('move',bind_move)
    wss.hand('motor',bind_motor)
    wss.hand('action',bind_action)
    wss.hand('chika',bind_chika) # actually, it's used to do heartbeat...
    wss.loop()

