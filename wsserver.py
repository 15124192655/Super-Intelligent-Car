# --coding:utf-8--

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import socket
import urllib
from car_controler import FourWheelDriveCar
import asyncio
import websockets


carControler = FourWheelDriveCar()

async def bind(websocket,path):
    while True:
        name=await websocket.recv()
        print(f"recv {name}")
        carControler.carMove(name)

wbserver=websockets.serve(bind,'127.0.0.1',9090)

asyncio.get_event_loop().run_until_complete(wbserver)
asyncio.get_event_loop().run_forever()


