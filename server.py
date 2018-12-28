# --coding:utf-8--

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import socket
import urllib
from car_controler import FourWheelDriveCar
import asyncio
import websockets

class CarServer(BaseHTTPRequestHandler):
    carControler = FourWheelDriveCar()

    def get_host_ip(self):
        '''
        This method is used for getting local ip address
        The car server will deploy on this ip
        '''
        try:
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            serverSocket.connect(("8.8.8.8", 80))
            localIP = serverSocket.getsockname()[0]
        finally:
            return localIP

    def do_GET(self):
        '''
        Define the car control GUI for client
        For the first edition, it will only return direction contol GUI
        '''
        localIP = CarServer.get_host_ip(self)

        # When this GET method is called, then should init the car
        self.carControler.reset()

        # Read control page html file from control.html
        controlPageFile = open("control.html")
        controlPageGUI = controlPageFile.read()
        controlPageFile.close()
        controlPageGUI = controlPageGUI.replace(
            "requestAddress", "http://" + localIP + ":9090/")

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(controlPageGUI.encode())

    def do_POST(self):

        length = int(self.headers['Content-Length'])
        qs = self.rfile.read(length)
        direction = qs.decode()

        print(direction)
            # This is used to control the car
        self.carControler.carMove(direction)
        self.send_response(200)
        
        self.end_headers()

async def bindhttp(server):
    server.serve_forever()
if __name__ == "__main__":
    raspCarServer = CarServer
    hostIP = raspCarServer.get_host_ip(raspCarServer)
    hostPort = 9090
    myServer = HTTPServer((hostIP, hostPort), raspCarServer)

    print(time.asctime(), "Server Starts - %s:%s" % (hostIP, hostPort))

    asyncio.get_event_loop().run_until_complete(bindhttp())
    asyncio.get_event_loop().run_forever()


'''
async def bind(websocket,path):
    while True:
        name=await websocket.recv()
        print(f"< {name}")

wbserver=websockets.serve(bind,'127.0.0.1',8765)

asyncio.get_event_loop().run_until_complete(wbserver)
#asyncio.get_event_loop().run_forever()
'''
