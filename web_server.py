import asyncio		#asynchronous
import datetime		#get time stamp
import random		#make random number
import websockets	#main stuff

async def myServ(ws, path):
    while True:
        now = 'e1800920 ' + datetime.datetime.utcnow().isoformat()
        await ws.send(now)
        await asyncio.sleep(1 + random.random() * 3)

start_server = websockets.serve(myServ, "192.168.1.212", 11111)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
