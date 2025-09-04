from channels.generic.websocket import AsyncWebsocketConsumer,WebsocketConsumer
import json
from asgiref.sync import async_to_sync 

class MyConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = "test_consumer_group"

        # group এ যোগ করুন
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        # client কে প্রথম message পাঠান
        self.send(text_data=json.dumps({'status': 'connected'}))

    def disconnect(self, close_code):
        # group থেকে বের করুন
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        print(text_data)
        data = json.loads(text_data)
        message = data.get('message', '')

        # সরাসরি client কে echo করুন
        self.send(text_data=json.dumps({
            'message': message
        }))

    def send_notification(self,event):
        print("Event Ready")
        print(event)
        data =event.get('value')
        self.send(text_data=json.dumps({'payload':data}))



# class MyConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         message = data.get('message', '')
#         await self.send(text_data=json.dumps({
#             'message': message
#         }))
