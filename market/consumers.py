from channels.generic.websocket import AsyncJsonWebsocketConsumer


class NoseyConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("gossip", self.channel_name)
        print("Added {} channel to gossip".format(self.channel_name))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("gossip", self.channel_name)
        print("Removed {} channel to gossip".format(self.channel_name))

    async def user_gossip(self, event):
        await self.send_json(event)
        print("Got message {} at {}".format(event, self.channel_name))