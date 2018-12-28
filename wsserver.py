# --coding:utf-8--

import asyncio
import websockets
import json
class WsServer:
    async def bind(self,websocket,path):
        while True:
            data=await websocket.recv()
            if(self.debug):print(f"recv {data}")
            dec=json.loads(data)
            # {'handle':'?',...}
            if dec['handle'] in self.handle.keys():
                self.handle[dec['handle']](dec)

    def __init__(self,port,debug=False):
        self.wbserver=websockets.serve(self.bind,'127.0.0.1',port)
        self.debug=debug
        self.handle={}

    def loop_sync(self):
        asyncio.get_event_loop().run_until_complete(self.wbserver)
        print("server is running")
    
    def loop(self):
        self.loop_sync()
        asyncio.get_event_loop().run_forever()

    def hand(self,key,func):
        self.handle[key]=func

if __name__=="__main__":
    ws=WsServer('9090',True)
    def test(data):
        print("yes")
    ws.hand("test",test)
    ws.loop()
