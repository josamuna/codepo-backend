#   Connection Return Codes
#   0: Connection successful
#   1: Connection refused: incorrect protocol version
#   2: Connection refused: invalid client identifier
#   3: Connection refused: server unavailable
#   4: Connection refused: bad username or password
#   5: Connection refused: not authorised
#   6-255: Currently unused.

from datetime import datetime

from celery import shared_task
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils import timezone
from paho.mqtt import client as mqtt_client

from .models import Measured, Device, DeviceTracking, Notification
from .serializers import MeasuredSerializer

import time
import threading

# generate client ID with pub prefix randomly
# client_id = f'python-mqtt-{random.randint(0, 1000)}'

# Clients list for production
clients = [
    {"broker":"mqtt.thingstream.io", "port":1883, "client_id":"device:21934b3c-da9e-431d-8b89-8695b3ac77f2", "topic":"FICT8C79", "username":"QLOSFKZU5WFI2F9Z1XHR", "password":"eLK678pvgtOttN2xxv+bIEKsl/jOXzd/8ubM+G6l"},
    {"broker":"mqtt.thingstream.io", "port":1883, "client_id":"device:ec893223-df92-404b-ba96-c7c085cb16f9", "topic":"FICT8C80", "username":"QLOSFKZU5WFI2F9Z1XHR", "password":"f3Fu7pLG1ZKr1/9lAZl5W7xTX3Vlfb4IziWkcbTk"},
    {"broker":"mqtt.thingstream.io", "port":1883, "client_id":"device:9c58f221-1205-4702-83ba-3408d399c587", "topic":"FICT8C81", "username":"QLOSFKZU5WFI2F9Z1XHR", "password":"1OVjWz37pOOGNgx5tbhHSxGyi/8YS+arppi5zZLi"}
] 

# Clients list for test only
""" clients = [
    {"broker":"broker.emqx.io", "port":1883, "client_id":"device:21934b3c-da9e-431d-8b89-8695b3ac77f2", "topic":"FICT8C79", "username":"QLOSFKZU5WFI2F9Z1XHR", "password":"eLK678pvgtOttN2xxv+bIEKsl/jOXzd/8ubM+G6l"},
    {"broker":"broker.emqx.io", "port":1883, "client_id":"python-mqtt-200", "topic":"FICT8C80", "username":"QLOSFKZU5WFI2F9Z1XHR", "password":"f3Fu7pLG1ZKr1/9lAZl5W7xTX3Vlfb4IziWkcbTk"},
    {"broker":"broker.emqx.io", "port":1883, "client_id":"python-mqtt-300", "topic":"my_topic", "username":"QLOSFKZU5WFI2F9Z1XHR", "password":"1OVjWz37pOOGNgx5tbhHSxGyi/8YS+arppi5zZLi"}
] """

# Set number of clients
nbr_clients = len(clients)

# Handle multi-connections to the Broker
def connect_mqtts():
    all_clients = []
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            client.connected_flag = True
            print("'" + c["client_id"] + "' Connected to MQTT Broker '" + c["broker"] + "' successfully!!!")
        else:
            print("Failed to connect client '" + c["client_id"] + "', return code " + str(rc))
    
    for c in clients:
        mqtt_client.Client.connected_flag = False
        client = mqtt_client.Client(c["client_id"], clean_session=False)
        client.username_pw_set(c["username"], c["password"])
        client.on_connect = on_connect
        client.loop_start()
        client.connect(c["broker"], c["port"])

        while not client.connected_flag:
            print('------------Wainting to be connected----------------')
            time.sleep(1)
        
        all_clients.append(client)
        
    return all_clients


# Subscribe multiples clients to topic
def subscribes(all_clients):
    def on_message(client, userdata, msg):
        print(str(msg.payload))
        msg_processed = __process_msg(str(msg.payload))
        print(msg_processed)
        if len(msg_processed) > 5:
            result = updateDevice(msg_processed)
            if result:
                saveMeasure(msg_processed)
    i = 0
    for c in all_clients:
        c.subscribe(clients[i]["topic"])
        c.on_message = on_message
        time.sleep(2)
        disconnect(c, i)
        i = i + 1


# Handle one connection to the Broker
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            client.connected_flag = True
            print("'" + clients[0]["client_id"] + "' Connected to MQTT Broker '" + clients[0]["broker"] + "' successfully!!!")
        else:
            print("Failed to connect client '" +  clients[0]["client_id"] + "', return code " + str(rc))
    mqtt_client.Client.connected_flag = False
    client = mqtt_client.Client(clients[0]["client_id"], clean_session=False)
    client.username_pw_set(clients[0]["username"], clients[0]["password"])
    client.on_connect = on_connect
    client.loop_start()
    # client.tls_set()
    client.connect(clients[0]["broker"], clients[0]["port"])

    while not client.connected_flag:
        print('------------Wainting to be connected----------------')
        time.sleep(1)
    #client.loop_stop()
    return client


# Subscribe one client to topic
def subscribe(client):
    def on_message(client, userdata, msg):
        current_topic = msg.topic
        msg_processed = __process_msg(str(msg.payload))  
        
        if(current_topic == clients[0]["topic"] or current_topic == clients[1]["topic"] or current_topic == clients[2]["topic"]):
            print("\n=>Message = " + str(msg_processed) + "\n=>Topic = " + msg.topic)
            if len(msg_processed) > 5:
                result = updateDevice(msg_processed)
                if result:
                    saveMeasure(msg_processed)
        else:
            print("Bad topic provided!!")
            # raise Exception("Bad topic provided!!") 

    client.subscribe([(clients[0]["topic"] , 1), (clients[1]["topic"], 1)])
    client.on_message = on_message
    time.sleep(1)
    disconnect(client, 0)

# Handle diconnection (Single or multiple) to the Broker
def disconnect(client, num_client):
    def on_disconnect(client, userdata, rc):
        if rc == 0:
            print("'" + clients[num_client]["client_id"] + "' Disconnected to MQTT Broker '" + clients[num_client]["broker"] + "' successfully!!!")
        else:
            print("Failed to disconnect client '" +  clients[num_client]["client_id"] + "', return code " + str(rc))
    client.on_disconnect = on_disconnect
    client.disconnect()


# We can have either registered task | Start task
@shared_task
def connect_to_mqtt_broker():
    try:
        print('Attempting to connect...')
        client = connect_mqtt()
        subscribe(client)

        # Multiples connections
        """ print('Attempting to connect...')
        all_clients = connect_mqtts()
        subscribes(all_clients) """
    except Exception as e:
        print("Error occurs while processing task " + str(e))
 
# @shared_task 
@shared_task
def send_notification():
    print('Here I\'m')
    # Another trick


def updateDevice(msg_processed):
    try:
        caseid = str(msg_processed['caseid']).strip() if msg_processed.get("caseid") is not None else 0
        if msg_processed.get("caseid") is not None and msg_processed.get("mode") is not None:
            my_device = Device.objects.get(caseid=caseid)
            mode = str(msg_processed['mode']).strip()
            if len(mode) >= 1:
                is_numeric = str(mode).isnumeric()
                if is_numeric:
                    is_valid_interval = int(mode) < 5
                    if my_device and is_valid_interval:
                        battery_mode = {
                            1: 'BAT_GPS',
                            2: 'BAT',
                            3: 'ECONOMY',
                            4: 'CALIBRATION'
                        }
                        my_device.mode = battery_mode[int(mode)]

                        if int(mode) == 4:
                            my_device.interval_bat_s = None
                            my_device.interval_sending_h = None
                            # my_device.autonomy = None
                            my_device.autonomy = 0
                        else:
                            my_device.interval_bat_s = str(msg_processed['interval_bat_s']).strip() if msg_processed.get(
                                "interval_bat_s") is not None else my_device.interval_bat_s
                            my_device.interval_sending_h = str(
                                msg_processed['interval_sending_h']).strip() if msg_processed.get(
                                "interval_sending_h") is not None else my_device.interval_sending_h
                            my_device.autonomy = str(msg_processed['autonomy']).strip() if msg_processed.get(
                                "autonomy") is not None else my_device.interval_sending_h

                        my_device.save()

                        print('Device properties updated')
                        return True
    except Exception as exc:
        print(f"Error occured when trying to update device properties : {exc}")
        return False


def saveMeasure(msg_processed):
    try:
        longitude = msg_processed.get('longitude')
        latitude = msg_processed.get('latitude')
        soc = msg_processed.get("soc")
        autonomy = msg_processed.get("autonomy")
        caseid = str(msg_processed['caseid']).strip() if msg_processed.get("caseid") is not None else 0
        if msg_processed.get("caseid") is not None and msg_processed.get("soc") is not None:
            my_device = Device.objects.get(caseid=caseid)
            soc = str(msg_processed.get("soc")).strip()
            is_not_none = msg_processed.get('latitude') is not None and msg_processed.get('longitude') is not None
            is_invalid_length = len(msg_processed.get('latitude')) < 2 and len(msg_processed.get('longitude')) < 2
            is_na_n = str(msg_processed.get('latitude')).strip().lower() == 'nan' or str(
                msg_processed.get('longitude')).strip().lower()
            if soc.isnumeric():
                if is_not_none or is_invalid_length or is_na_n:
                    measure = Measured.objects.filter(device_id=my_device).order_by('-id')[:1]
                    if measure:
                        for m in measure:
                            longitude = m.longitude
                            latitude = m.latitude

                measured_data = {
                    'latitude': latitude,
                    'longitude': longitude,
                    'soc': soc,
                    'time': datetime.now(),
                    'device_id': my_device.id,
                }

                measured_serializer = MeasuredSerializer(data=measured_data)
                if measured_serializer.is_valid():
                    measured_serializer.save()
                    print('Measured saved successfully')

                    # Save Notifications
                    try:
                        __saveNotification(caseid, autonomy, soc)
                    except Exception as exc:
                        print(f"Error save notification : {exc}")

                    # When values are valid we try to send an email   
                    try: 
                        __sendMail(caseid, autonomy, soc)
                    except Exception as exc:
                        print(f"Error while sending mail : {exc}")
                else:
                    print(measured_serializer.errors)
    except Exception as exc:
        print(f"Error occured when trying to save measure : {exc}")


def __process_msg(msg):
    new_msg = msg.replace('{', '')
    new_msg = new_msg.replace('}', '')
    new_msg = new_msg.split(',')
    data = {}
    try:
        for val in new_msg:
            new_val = val.split(':')
            if len(new_val) > 1:
                if 'caseid' in str(new_val[0]).lower():
                    data['caseid'] = str(new_val[1]).strip()
                elif 'soc' in str(new_val[0]).lower():
                    data['soc'] = str(new_val[1]).strip()
                elif 'latitude' in str(new_val[0]).lower():
                    data['latitude'] = str(new_val[1]).strip()
                elif 'longitude' in str(new_val[0]).lower():
                    data['longitude'] = str(new_val[1]).strip()
                elif 'mode' in str(new_val[0]).lower():
                    data['mode'] = str(new_val[1]).strip()
                elif 'interval_bat_s' in str(new_val[0]).lower():
                    data['interval_bat_s'] = str(new_val[1]).strip()
                elif 'interval_sending_h' in str(new_val[0]).lower():
                    new_val[1] = str(new_val[1]).replace("'", '')
                    new_val[1] = str(new_val[1]).replace('"', '')
                    data['interval_sending_h'] = str(new_val[1]).strip()
                elif 'autonomy' in str(new_val[0]).lower():
                    new_val[1] = str(new_val[1]).replace("'", '')
                    new_val[1] = str(new_val[1]).replace('"', '')
                    data['autonomy'] = str(new_val[1]).strip()
    except Exception as exc:
        print("Error occurred. Format message is not valid")
    return data


def __saveNotification(caseid, autonomy, soc):
    if(float(soc) <= 50):
        data = __setNotificationParams(soc, autonomy)
        notification = data['notification_message']
        dev = Device.objects.get(caseid=caseid)
        if dev:
            dev_track = DeviceTracking.objects.filter(device_id=dev.id).values('user_id').distinct()
            for d in dev_track:
                user = User.objects.get(pk=d['user_id'])
                notif = Notification(
                    notification=notification,
                    time=timezone.now(),
                    device_id=dev,
                    user_id=user,
                    status=False,
                    caseid=caseid
                )
                notif.save()
            print("Notifications saved successfully")


# Specify email content message and subject
def __setEmailMessageParams(soc, autonomy):
    data  = {}
    data['email_message'] = "Alerte malette MSF"
    data['subject_email'] = f"The battery level is currently at {soc}%. The estimated time remaining is {autonomy}heure(s)".format(
        soc)
    return data


# Specify notification content message
def __setNotificationParams(soc, autonomy):
    data  = {}
    data['notification_message'] = f"The battery level is currently at {soc}%. The estimated time remaining is {autonomy}"
    return data


# The mail has sent only if the SOC level is less than or egal 50 or soc <= 50
def __sendMail(caseid, autonomy, soc):
    email_from = settings.EMAIL_HOST_USER
    data = {}
    if(float(soc) <= 50):
        if (email_from != 'EMAIL_HOST_USER' or email_from != None):
            data = __setEmailMessageParams(soc, autonomy)
            
            dev = Device.objects.get(caseid=caseid)
            email_list = []
            if dev:
                dev_track = DeviceTracking.objects.filter(device_id=dev.id).values('user_id').distinct()
                for d in dev_track:
                    user = User.objects.get(pk=d['user_id'])
                    email_list.append(user.email)
            if email_list:
                subject_email = data['subject_email']
                email_message = data['email_message']
                send_mail(subject_email, email_message, email_from, email_list)
                print("Mails sent successfully")       
