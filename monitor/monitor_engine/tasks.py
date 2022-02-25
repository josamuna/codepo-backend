#   Connection Return Codes
#   0: Connection successful
#   1: Connection refused – incorrect protocol version
#   2: Connection refused – invalid client identifier
#   3: Connection refused – server unavailable
#   4: Connection refused – bad username or password
#   5: Connection refused – not authorised
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

broker = "broker.emqx.io"
# broker = "mqtt.thingstream.io"
topic = "FICT8C79"
port = 1883
# topic = "DtW"

# generate client ID with pub prefix randomly
# client_id = f'python-mqtt-700'
# client_id = f'python-mqtt-{random.randint(0, 1000)}'
client_id = "device:21934b3c-da9e-431d-8b89-8695b3ac77f2"
username = "QLOSFKZU5WFI2F9Z1XHR"
password = "eLK678pvgtOttN2xxv+bIEKsl/jOXzd/8ubM+G6l"
flag_connected = 0

# Handle connection to the Broker
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            client.connected_flag = True
            print("Connected to MQTT Broker '" + broker + "' successfully!!!")
        else:
            print("Failed to connect, return code " + str(rc))
    mqtt_client.Client.connected_flag = False
    client = mqtt_client.Client(client_id, clean_session=False)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.loop_start()
    # client.tls_set()
    client.connect(broker, port)

    while not client.connected_flag:
        print('------------Wainting to be connected----------------')
        time.sleep(1)
    #client.loop_stop()
    return client


def subscribe(client):
    def on_message(client, userdata, msg):
        print(str(msg.payload))
        msg_processed = process_msg(str(msg.payload))
        print(msg_processed)
        if len(msg_processed) > 5:
            updateDevice(msg_processed)
            saveMeasure(msg_processed)
            saveNotification(msg_processed) 
            # This line must be decommented after adding e-mail credentials
            # sendMail(msg_processed)

    client.subscribe(topic)
    client.on_message = on_message
    time.sleep(1)
    disconnect(client)

# Handle diconnection to the Broker
def disconnect(client):
    def on_disconnect(client, userdata, rc):
        if rc == 0:
            print("Disconnected to MQTT Broker '" + broker + "' successfully!!!")
        else:
            print("Failed to disconnect, return code " + str(rc))
    client.on_disconnect = on_disconnect
    client.disconnect()


# We can have either registered task
@shared_task
def connect_to_mqtt_broker():
    print('Attempting to connect...')
    client = connect_mqtt()
    subscribe(client)  


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
                            my_device.autonomy = None
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
    except Exception as exc:
        print(f"Error occured when trying to update device properties : {exc}")


def saveMeasure(msg_processed):
    try:
        longitude = msg_processed.get('longitude')
        latitude = msg_processed.get('latitude')
        soc = msg_processed.get("soc")
        # autonomy = msg_processed.get("soc")
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
                else:
                    print(measured_serializer.errors)
    except Exception as exc:
        print(f"Error occured when trying to save measure : {exc}")


def process_msg(msg):
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


def saveNotification(msg_processed):
    try:
        if msg_processed.get('soc') is not None and len(msg_processed.get('soc')) > 1:
            if float(msg_processed.get('soc').strip()) <= 50:
                caseid = msg_processed.get('caseid')
                soc = msg_processed.get('soc').strip()
                autonomy = msg_processed.get('autonomy').strip()
                notification = f"The battery level is currently at {soc}%. The estimated time remaining is {autonomy}"
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
    except Exception as exc:
        print(f"Error save notification : {exc}")


def sendMail(msg_processed):
    try:
        if msg_processed.get('soc') is not None and len(msg_processed.get('soc')) > 1:
            if float(msg_processed.get('soc').strip()) <= 50:
                caseid = msg_processed.get('caseid').strip()
                soc = msg_processed.get('soc').strip()
                autonomy = msg_processed.get('autonomy').strip()
                subject = "Alerte malette MSF"
                message = f"The battery level is currently at {soc}%. The estimated time remaining is {autonomy}heure(s)".format(
                    soc)
                email_from = settings.EMAIL_HOST_USER
                dev = Device.objects.get(caseid=caseid)
                email_list = []
                if dev:
                    dev_track = DeviceTracking.objects.filter(device_id=dev.id).values('user_id').distinct()
                    for d in dev_track:
                        user = User.objects.get(pk=d['user_id'])
                        email_list.append(user.email)
                if email_list:
                    send_mail(subject, message, email_from, email_list)
                    print("Mails sent successfully")
    except Exception as exc:
        print(f"Error send mail : {exc}")
