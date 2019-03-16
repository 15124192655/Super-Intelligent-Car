# --coding:utf-8--
import asyncio
import websockets
import json
import logging
class Data:
    def __init__(self,handle):
        self.data={}
        self.data['handle']=handle
    async def send(self,ws):
        await ws.send(json.dumps(self.data))
    def add(self,id,val):
        self.data[id]=val
        return self

class WsServer:
    async def bind(self,websocket,path):
        logging.info('receive connection from %s' % (path))
        while True:
            #try:
                data=await websocket.recv()
                logging.info("receive %s"%data)
                dec=json.loads(data)
                # {'handle':'?',...}
                if dec['handle'] in self.handle.keys():
                    await self.handle[dec['handle']](dec,websocket)#TODO: simplify websocket?
            #except:
            #    logging.info('connection closed')
            #    break
        # while end
    #bind end

    def __init__(self,port,debug=False):
        self.wbserver=websockets.serve(self.bind,'0.0.0.0',port)
        self.debug=debug
        self.handle={}

    def loop_sync(self):
        asyncio.get_event_loop().run_until_complete(self.wbserver)
        logging.info('server is running')
    
    def loop(self):
        self.loop_sync()
        asyncio.get_event_loop().run_forever()

    def hand(self,key,func):
        self.handle[key]=func

if __name__=="__main__":
    logging.basicConfig(level=logging.DEBUG)
    ws=WsServer('9090',True)
    async def test(data,ws):
        await Data("test").add('msg',data['msg']).send(ws)
    ws.hand("test",test)
    ws.loop()
