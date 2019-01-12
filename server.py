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

    
    wss.hand('move',bind_move)
    wss.loop()

