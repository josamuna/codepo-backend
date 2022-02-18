# from django.shortcuts import render,HttpResponse
import datetime
import json

from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.http.response import JsonResponse
from paho.mqtt import client as mqtt_client
# from rest_framework.parsers import JSONParser
# from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

# from .models import Command, Device, Measured
from .serializers import *

# from .consumers import MqttConsumer

#####################################
#  COMMUNICATION MQTT WITH DEVICES  #
#####################################

# broker = 'broker.emqx.io'
broker = "mqtt.thingstream.io"
port = 1883
# topic = "/python/mqtt/help"
topic = "FICT8C79"

# generate client ID with pub prefix randomly
# client_id = f'python-mqtt-{random.randint(0, 1000)}'
client_id = "device:21934b3c-da9e-431d-8b89-8695b3ac77f2"
username = "QLOSFKZU5WFI2F9Z1XHR"
password = "eLK678pvgtOttN2xxv+bIEKsl/jOXzd/8ubM+G6l"


###################################
#   ALL VIEWS RELATED TO DEVICES  #
###################################

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllDevices():
    devices = Device.objects.filter(deleted=False)
    devices_serializer = DeviceSerializer(devices, many=True)
    return JsonResponse(devices_serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getDeviceById(pk):
    device = Device.objects.get(pk=pk)
    device_serializer = DeviceSerializer(device)
    return JsonResponse(device_serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createDevice(request):
    status = {'status': False}
    device_serializer = DeviceSerializer(data=request.data)
    if device_serializer.is_valid():
        caseid = device_serializer.validated_data['caseid']
        mode = device_serializer.validated_data['mode']
        interval_bat_s = device_serializer.validated_data['interval_bat_s']
        interval_sending_h = device_serializer.validated_data['interval_sending_h']
        total_capacity = 0
        created_by = 0
        if (device_serializer.validated_data['created_by']):
            created_by = device_serializer.validated_data['created_by']
        dev_list = Device.objects.filter(caseid=caseid)
        if not dev_list:
            device = Device(
                caseid=caseid,
                mode=mode,
                interval_bat_s=interval_bat_s,
                interval_sending_h=interval_sending_h,
                total_capacity=total_capacity,
                created_by=created_by
            )
            device.save()
            status = {'status': True, 'message': 'Device saved succefully'}
        else:
            status = {'status': False, 'message': 'Device with the some identity already exists'}
    else:
        status = {'status': False, 'message': 'Device data are not valid {0}'.format(device_serializer.errors)}
    return JsonResponse(status)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateDevice(request, **kwargs):
    pk = kwargs['pk']
    status = {'status': False}
    device = Device.objects.get(id=pk)
    device_serializer = DeviceSerializer(instance=device, data=request.data)
    if device_serializer.is_valid():
        caseid = device_serializer.validated_data['caseid']
        mode = device_serializer.validated_data['mode']
        interval_bat_s = device_serializer.validated_data['interval_bat_s']
        interval_sending_h = device_serializer.validated_data['interval_sending_h']
        total_capacity = 0
        updated_by = 0
        if device_serializer.validated_data.get('updated_by'):
            updated_by = device_serializer.validated_data['updated_by']
        device = Device(
            id=device.id,
            caseid=caseid,
            mode=mode,
            interval_bat_s=interval_bat_s,
            interval_sending_h=interval_sending_h,
            total_capacity=total_capacity,
            created_at=device.created_at,
            updated_by=updated_by
        )
        device.save()
        status = {'status': True, 'message': 'Device updated succefully'}
    else:
        status = {'status': False, 'message': 'Device data are not valid'}
    return JsonResponse(status)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deleteDevice(request, pk):
    device = Device.objects.get(pk=pk)
    print(request.data.get('deleted_by'))
    if device:
        device.deleted = True
        device.deleted_at = datetime.datetime.now()
        if request.data.get('deleted_by'):
            device.deleted_by = request.data.get('deleted_by')
        device.save()
        status = {'status': True, 'message': 'Device deleted succefully'}
    else:
        status = {'status': False, 'message': 'Device does not exists'}
    return JsonResponse(status)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllDeletedDevices(request):
    devices = Device.objects.filter(deleted=True)
    devices_serializer = DeviceSerializer(devices, many=True)
    return JsonResponse(devices_serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restoreDevice(request, pk):
    device = Device.objects.get(pk=pk)
    if device:
        device.deleted = False
        device.save()
        status = {'status': True, 'message': 'Device restored succefully'}
    else:
        status = {'status': False, 'message': 'Device does not exists'}
    return JsonResponse(status)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def permanentlyDeleteDevice(request, pk):
    device = Device.objects.get(pk=pk)
    if device:
        device.delete()
        status = {'status': True, 'message': 'Device deleted succefully'}
    else:
        status = {'status': False, 'message': 'Device does not exists'}
    return JsonResponse(status)


def getNumberDevice(request):
    my_data = {}
    for p in Device.objects.raw(
            'SELECT 1 AS id, COUNT(*) as TOTAL, (SELECT COUNT(*) FROM `tb_device` WHERE `deleted`=0) AS ACTIVE FROM `tb_device`'):
        values = {'totalDevice': p.TOTAL, 'activeDevices': p.ACTIVE}
        my_data['data'] = values
    return JsonResponse(my_data)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def getFollowedDevices(request):
    # print(request.data)
    my_data = []
    user_id = request.data.get('user_id')
    sql = "SELECT id, time, isTrack, device_id,user_id FROM tb_device_tracking WHERE id IN (SELECT MAX(id) FROM `tb_device_tracking` WHERE user_id={0} GROUP BY device_id) AND user_id={1}".format(
        user_id, user_id)
    for p in DeviceTracking.objects.raw(sql):
        values = {'id': p.id, 'isTrack': p.isTrack, 'device_id': p.device_id.id, 'user_id': p.user_id.id}
        my_data.append(values)
    return JsonResponse(my_data, safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def followDevice(request):
    try:
        status = {'status': False}
        time = datetime.datetime.now()
        is_track = request.data['isTrack']
        device_id = request.data['device_id']
        user_id = request.data['user_id']
        user = User.objects.get(pk=user_id)
        device = Device.objects.get(pk=device_id)
        tracking = DeviceTracking(
            time=time,
            isTrack=is_track,
            device_id=device,
            user_id=user
        )
        tracking.save()
        status = {'status': True, 'message': 'Start device tracking'}
    except Exception as exc:
        status = {'status': False, 'message': 'An error occurred'}
        print(exc)
    return JsonResponse(status)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def saveColorPreference(request):
    try:
        status = {'status': False}
        lev1 = request.data.get('level_one')
        lev2 = request.data.get('level_two')
        lev3 = request.data.get('level_three')
        lev4 = request.data.get('level_four')
        user_id = request.data.get('user_id')
        user = User.objects.get(pk=user_id)
        p = UserPreference.objects.get(user_id=user)
        if p:
            p.level_one = lev1
            p.level_two = lev2
            p.level_three = lev3
            p.level_four = lev4
            p.save()
        else:
            pref = UserPreference(
                level_one=lev1,
                level_two=lev2,
                level_three=lev3,
                level_four=lev4,
                user_id=user
            )
            pref.save()
        status = {'status': True, 'message': 'Preference saved succefully'}
    except Exception as exc:
        status = {'status': False, 'message': 'Error occurred when trying to save color preference'}
        print(exc)
    return JsonResponse(status)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getColorPreference(request, pk):
    user = User.objects.get(pk=pk)
    user_preference = None
    prefs = None
    if user:
        user_preference = UserPreference.objects.get(user_id=user)
        prefs = UserPreferenceSerializer(user_preference)
    return JsonResponse(prefs.data, safe=False)


###################################
#   ALL VIEWS RELATED TO USERS    #
###################################

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllUsers(request):
    users = User.objects.filter(is_active=True)
    users_serializer = UserSerializer(users, many=True)
    return JsonResponse(users_serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserById(request, pk):
    user = User.objects.get(pk)
    user_serializer = UserSerializer(user)
    return JsonResponse(user_serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createUser(request):
    status = {'status': False}
    print(request.data)
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        user_name = user_serializer.validated_data['username']
        first_name = user_serializer.validated_data['first_name']
        last_name = user_serializer.validated_data['last_name']
        mail = user_serializer.validated_data['email']
        is_staff = user_serializer.validated_data['is_staff']

        users = User.objects.filter(
            Q(username=user_name) |
            Q(email=mail) |
            Q(first_name=first_name) & Q(last_name=last_name))
        if not users:
            # user_serializer.validated_data['password'] = set
            user_serializer.save()
            status = {'status': True, 'message': 'Saved user succefully'}
        else:
            status = {'status': False, 'message': 'User already exists'}
    else:
        status = {'status': False, 'message': user_serializer.errors}
    return JsonResponse(status)


@api_view(['POST'])
def updateUser(request, **kwargs):
    pk = kwargs['pk']
    status = {'status': False}
    user = User.objects.get(id=pk)
    user_serializer = UserSerializer(instance=user, data=request.data)
    if user_serializer.is_valid():
        pass_word = user_serializer.validated_data.get('password')
        user.username = user_serializer.validated_data['username']
        user.first_name = user_serializer.validated_data['first_name']
        user.last_name = user_serializer.validated_data['last_name']
        user.email = user_serializer.validated_data['email']
        user.is_staff = user_serializer.validated_data['is_staff']
        if len(pass_word) > 1:
            print('password is set')
            user.set_password(pass_word)
        user.save()
        status = {'status': True, 'message': 'User updated succefully'}
    else:
        # print(user_serializer.data['password'])
        status = {'status': False, 'message': 'User data are not valid'}
    return JsonResponse(status)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUser(request, pk):
    user = User.objects.get(pk=pk)
    if user:
        user.is_active = False
        user.save()
        status = {'status': True, 'message': 'User deleted succefully'}
    else:
        status = {'status': False, 'message': 'User does not exists'}
    return JsonResponse(status)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restoreUser(request, pk):
    user = User.objects.get(pk=pk)
    if user:
        user.is_active = True
        user.save()
        status = {'status': True, 'message': 'User restored succefully'}
    else:
        status = {'status': False, 'message': 'User does not exists'}
    return JsonResponse(status)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def permanentlyDeleteUser(request, pk):
    user = User.objects.get(pk=pk)
    if user:
        user.delete()
        status = {'status': True, 'message': 'User deleted succefully'}
    else:
        status = {'status': False, 'message': 'User does not exists'}
    return JsonResponse(status)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllDeleteUsers(request):
    users = User.objects.filter(is_active=False)
    users_serializer = UserSerializer(users, many=True)
    return JsonResponse(users_serializer.data, safe=False)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def loginUser(request):
    print(request.body)
    print("#############################")
    body = json.loads(request.body)
    item = body['item']
    print("item ====> {0}".format(item))
    # item = request.user.email
    user = User.objects.get((Q(username=item) | Q(email=item)))
    user_serializer = UserSerializer(user)
    # status = {'status': True, 'message': msg}
    return JsonResponse(user_serializer.data, safe=False)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getNumberUser(request):
    my_data = {}
    for p in User.objects.raw(
            'SELECT 1 as id, COUNT(*) AS TOTAL, (SELECT COUNT(*) FROM `auth_user` WHERE `is_active`) AS ACTIVE FROM `auth_user`'):
        values = {'totalUser': p.TOTAL, 'activeUsers': p.ACTIVE}
        my_data['data'] = values
    return JsonResponse(my_data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getUserNotification(request, pk):
    notify = Notification.objects.filter(user_id=pk, status=False)
    not_serializer = NotificationSerializer(notify, many=True)
    return JsonResponse(not_serializer.data, safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def alreadyRead(request, pk):
    notif = Notification.objects.get(pk=pk)
    if notif:
        notif.status = True
        notif.save()
        status = {'status': True}
    else:
        status = {'status': False, 'message': 'User does not exists'}
    return JsonResponse(status)


#####################################
#   ALL VIEWS RELATED TO COMMANDS   #
#####################################

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllCommands(request):
    cmds = Command.objects.filter(deleted=False)
    cmds_serialiser = CommandSerializer(cmds, many=True)
    return JsonResponse(cmds_serialiser.data, safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCommandById(request, pk):
    cmd = Command.objects.get(pk=pk)
    cmd_serializer = CommandSerializer(cmd)
    return JsonResponse(cmd_serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createCommand(request):
    status = {'status': False}
    cmd_serializer = CommandSerializer(data=request.data)
    if cmd_serializer.is_valid():
        commande = cmd_serializer.validated_data['command']
        cmds = Command.objects.filter(command=commande)
        if not cmds:
            cmd_serializer.save()
            status = {'status': True, 'message': 'Saved command succefully'}
        else:
            status = {'status': False, 'message': 'Command already exists'}
    else:
        status = {'status': False, 'message': 'Command data are not valid'}
    return JsonResponse(status)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateCommand(request, **kwargs):
    pk = kwargs['pk']
    status = {'status': False}
    cmd = Command.objects.get(id=pk)
    cmd_serializer = CommandSerializer(instance=cmd, data=request.data)
    if cmd_serializer.is_valid():
        cmd_serializer.save()
        status = {'status': True, 'message': 'Command updated succefully'}
    else:
        status = {'status': False, 'message': 'Command data are not valid'}
    return JsonResponse(status)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteCommand(request, pk):
    cmd = Command.objects.get(pk=pk)
    if cmd:
        cmd.deleted = True
        cmd.save()
        status = {'status': True, 'message': 'Command deleted succefully'}
    else:
        status = {'status': False, 'message': 'Command does not exists'}
    return JsonResponse(status)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restoreCommand(request, pk):
    cmd = Command.objects.get(pk=pk)
    if cmd:
        cmd.deleted = False
        cmd.save()
        status = {'status': True, 'message': 'Command restored succefully'}
    else:
        status = {'status': False, 'message': 'Command does not exists'}
    return JsonResponse(status)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def permanentlyDeleteCommand(request, pk):
    cmd = Command.objects.get(pk=pk)
    if cmd:
        cmd.delete()
        status = {'status': True, 'message': 'Command deleted succefully'}
    else:
        status = {'status': False, 'message': 'Command does not exists'}
    return JsonResponse(status)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllDeletedCommands(request):
    cmds = Command.objects.filter(deleted=True)
    cmds_serialiser = CommandSerializer(cmds, many=True)
    return JsonResponse(cmds_serialiser.data, safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def searchCommand(request):
    element = request.GET.get('searchField')
    cmds = Command.objects.filter(
        Q(command__icontains=element) |
        Q(description__icontains=element)
    )
    cmd_serializer = CommandSerializer(cmds, many=True)
    return JsonResponse(cmd_serializer.data)


def connect_admin(user):
    refresh = RefreshToken.for_user(user)
    access_token = refresh.access_token
    access_token.set_exp(lifetime=datetime.timedelta(days=1))

    return {
        'refresh': str(refresh),
        'access': str(access_token),
    }


@api_view(['POST'])
def publish_mqtt(request):
    status = {'status': False}

    # print(request.data)
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)

    battery_mode = {
        1: 'BAT_GPS',
        2: 'BAT',
        3: 'ECONOMY',
        4: 'CALIBRATION'
    }
    mode = str()

    for index, mode in battery_mode.items():
        if request.data['mode'] == mode:
            mode = index

    data = {
        'caseid': request.data['caseid'],
        'mode': mode,
        'interval_bat_s': request.data['intervalBat'],
        'interval_sending_h': request.data['intervalSend'],
    }

    my_topic = request.data['caseid']
    msg = "{0},".format(request.data['mode'])
    msg += "{0},".format(request.data['intervalBat'])
    msg += "{0}".format(request.data['intervalSend'])

    if mode == 4:
        data['total_capacity'] = request.data['total_capacity']
        data['percentage'] = request.data['percentage']
        msg += ",{0}".format(request.data['total_capacity'])
        msg += ",{0}".format(request.data['percentage'])
    # msg = "{&caseid&: FICT8C79, &soc&: 32, &latitude&: -1.6606898429, &longitude&: 29.45987621846, &mode&: BAT, &interval_bat_s&: 2, &interval_sending_h&: 2}"
    # result = client.publish(myTopic,msg, qos=0, retain=True)
    # result = client.publish(topic,msg, qos=0, retain=True)
    # result: [0, 1]
    # status = result[0]
    status = 0
    if status == 0:
        status = {'status': True, 'message': 'Command succefully published'}
        print(f"Send `{msg}` to topic `{my_topic}`")
    else:
        print(f"Failed to send message to topic {broker}")
    return JsonResponse(status)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getDeviceData(request):
    data = Measured.objects.all().raw("SELECT * FROM `tb_measured` GROUP BY `device_id`")
    measureds = MeasuredSerializer(data, many=True)
    return JsonResponse(measureds.data, safe=False)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getDeviceHistory(request, pk):
    data = Measured.objects.filter(device_id=pk)
    measureds = MeasuredSimpleSerializer(data, many=True)
    return JsonResponse(measureds.data, safe=False)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getLocationHistory(request):
    devices_id = Measured.objects.values('device_id').distinct()
    ids = list()
    for value in devices_id:
        ids.append(value['device_id'])
    data = Device.objects.filter(pk__in=ids)
    history = HistorySerializer(instance=data, many=True)
    return JsonResponse(history.data, safe=False)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getLocationDeviceHistory(request):
    # data = Measured.objects.select_related('device_id')
    data = Device.objects.filter(
        Q(id=1) |
        Q(id=2) |
        Q(id=6)
    )
    history = HistorySerializer(instance=data, many=True)
    return JsonResponse(history.data, safe=False)


# ##########################################################################
# ##########################################################################
# ##########################################################################
# ##########################################################################


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    # print("===== Inside connection mqtt =====")
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    # client.tls_set()
    client.connect(broker, port)
    return client


# def subscribe(client: mqtt_client):
#     def on_message(client, userdata, msg):
#         payloads = json.loads(msg.payload)
#         print(payloads)
#         data = {
#             'location_latitude': payloads['lat'],
#             'location_longitude': payloads['long'],
#             'source': payloads['source'],
#             'tension': payloads['bat'],
#             'time': payloads['time'],
#             'device_id': payloads['device']
#         }
#         measuredSerializer = MeasuredSerializer(data=data)
#         if measuredSerializer.is_valid():
#             measuredSerializer.save()
#         # mqtt = MqttConsumer()
#         # mqtt.send_message(data)
#     print('===== Inside subscribe =====')
#     client.subscribe(topic)
#     client.on_message = on_message

# def init_mqtt_listen():
#     client = connect_mqtt()
#     subscribe(client)
#     client.loop_start()

@api_view(['POST'])
def sendMail(request):
    status = {'status': False}
    try:
        subject = "Alerte message MSF"
        message = "The battery level of FICT5678 is 23% now. His autonomy is estimated to 3h45"
        emails = ['nturumoussa@gmail.com', 'vitaltakanic@gmail.com']
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message, email_from, emails)
        status = {'status': True, 'message': 'Mails sent succefully'}
    except Exception as exc:
        status = {'status': False, 'message': 'Error occurred when trying to sent mails'}
        print(exc)
    return JsonResponse(status)
