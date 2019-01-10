# --coding:utf-8--
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import socket
import urllib
from car_controler import FourWheelDriveCar
import asyncio
import websockets
import wsserver
import json
carControler = FourWheelDriveCar()

if __name__ == "__main__":
    wss=WsServer('9090',True)
    def bind_move(data,ws):
        r1,r2=carControler.carMove(data['direction'])
        ws.send(json.dumps({'handle':'move','status':r2}))

    
    wss.hand('move',bind_move)
    wss.loop()

