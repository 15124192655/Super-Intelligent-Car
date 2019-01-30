# --coding:utf-8--
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import socket
import urllib
from fakecar_controller import FourWheelDriveCar
import asyncio
import websockets
from wsserver import WsServer
import json
import logging
carControler = FourWheelDriveCar()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    wss=WsServer('9090',True)
    async def bind_move(data,ws):
        r1,r2=carControler.carMove(data['direction'])
        await ws.send(json.dumps({'handle':'move','status':r2}))
    
    async def bind_motor(data,ws):
        '''
        TODO:we suppose the command is a series of movements encoding as an arrays including index and angle of each one.
        but now, it is just one single movement.
        '''
        carControler.setmotor(data['id'],data['angle'])
        logging.info('setmotor %s %s'%(data['id'],data['angle']))
    async def bind_chika(data,ws):
        # chika kawai!
        await ws.send(json.dumps({'handle':'chika','msg':'#0 yo-i yo-i'}))
        await ws.send(json.dumps({'handle':'chika','msg':'#1 do-nda yo!'}))
        await ws.send(json.dumps({'handle':'chika','msg':'#hope we can get ordered messages#'}))



    
    wss.hand('move',bind_move)
    wss.hand('motor',bind_motor)
    wss.hand('chika',bind_chika)
    wss.loop()

