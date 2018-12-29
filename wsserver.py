# --coding:utf-8--
import asyncio
import websockets
import json
class Data:
    def __init__(self,handle):
        self.data['handle']=handle
    async def send(self,ws):
        await ws.send(json.dumps(self.data))
class WsServer:
    async def bind(self,websocket,path):
        print('receive connection from ',path)
        while True:
            try:
                data=await websocket.recv()
                if(self.debug):print(f"recv {data}")
                dec=json.loads(data)
                # {'handle':'?',...}
                if dec['handle'] in self.handle.keys():
                    await self.handle[dec['handle']](dec,websocket)#TODO: simplify websocket?
            except websocket.exceptions.ConnectionClosed:
                print('connection closed ',path)
                break
        # while end
    #bind end

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
    async def test(data,ws):
        print('test')
        await ws.send(json.dumps({'handle':'test','msg':data['msg']}))
    ws.hand("test",test)
    ws.loop()
