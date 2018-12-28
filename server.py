# --coding:utf-8--

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import socket
import urllib
from car_controler import FourWheelDriveCar

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

if __name__ == "__main__":
    raspCarServer = CarServer
    hostIP = raspCarServer.get_host_ip(raspCarServer)
    hostPort = 9090
    myServer = HTTPServer((hostIP, hostPort), raspCarServer)

    print(time.asctime(), "Server Starts - %s:%s" % (hostIP, hostPort))

    try:
        myServer.serve_forever()
    except KeyboardInterrupt:
        pass
