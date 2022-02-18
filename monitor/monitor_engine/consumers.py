import json
import random

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from paho.mqtt import client as mqtt_client

from .serializers import MeasuredSerializer


#####################################
#  COMMUNICATION MQTT WITH DEVICES  #
#####################################

class MqttConsumer(WebsocketConsumer):
    broker = 'broker.emqx.io'
    port = 1883
    topic = "/python/mqtt/help"

    # generate client ID with pub prefix randomly
    client_id = f'python-mqtt-{random.randint(0, 1000)}'

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!!!!!")
            else:
                print("Failed to connect, return code %d\n", rc)

        # print("===== Inside connection mqtt =====")
        client = mqtt_client.Client(self.client_id)
        # client.username_pw_set(username, password)
        client.on_connect = on_connect
        # client.tls_set()
        client.connect(self.broker, self.port)
        return client

    def subscribe(self, client: mqtt_client):
        def on_message(client, userdata, msg):
            payloads = json.loads(msg.payload)
            print(payloads)
            # print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            # self.send_message(text_data=json.dumps(msg.payload.decode()))
            data = {
                'location_latitude': payloads['lat'],
                'location_longitude': payloads['long'],
                'source': payloads['source'],
                'tension': payloads['bat'],
                'time': payloads['time'],
                'device_id': payloads['device']
            }
            measured_serializer = MeasuredSerializer(data=data)
            if measured_serializer.is_valid():
                measured_serializer.save()
            self.send_message({'from': 'backend', 'command': 'update_state', 'message': data})

        print('===== Inside subscribe =====')
        client.subscribe(self.topic)
        client.on_message = on_message

    def init_mqtt_listen(self, data):
        username = data['username']
        # user, created = User.objects.get_or_create(username=username)
        content = {
            'command': 'init_mqtt_listen'
        }
        client = self.connect_mqtt()
        self.subscribe(client)
        client.loop_start()
        print(username + ' connected succefully')
        # if not user:
        #     content['error'] = 'Unable to get or create User with username: ' + username
        #     self.send_message(content)
        # content['success'] = 'Chatting in with success with username: ' + username
        # self.send_message(content)

    def fetch_messages(self, data):
        # messages = Message.last_50_messages()
        print("Received message succefully")
        print(data)
        content = {
            'command': 'messages',
            'messages': 'machin'
            # self.messages_to_json(messages)
        }
        self.send_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            'id': str(message.id),
            'author': message.author.username,
            'content': message.content,
            'created_at': str(message.created_at)
        }

    commands = {
        'init_mqtt_listen': init_mqtt_listen,
        'fetch_messages': fetch_messages,
        # 'new_message': new_message
    }

    def connect(self):
        self.room_name = 'room'
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(room_group_name)
        self.accept()

    def disconnect(self, close_code):
        # leave group room
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        print("Received message succefully")
        print(data)
        content = {
            'command': 'messages',
            'messages': 'machin'
            # self.messages_to_json(messages)
        }
        self.send_message(content)
        # self.commands[data['command']](self, data)

    def send_message(self, message):
        self.send(text_data=json.dumps(message))
