from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Device, Command, Measured, DeviceTracking, UserPreference, Notification


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

    # def create(self, validated_data):
    #     device = Device(
    #         designation = validated_data['designation'],
    #         external_id = validated_data['external_id'],
    #         identity =  validated_data['identity']
    #     )
    #     device.save()
    #     return device


class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'password', 'is_active', 'is_superuser', 'is_staff')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=make_password(validated_data['password']),
            is_staff=validated_data['is_staff']
        )
        user.save()
        return user


class FilteredMeasuredSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        # print("=============================");
        mydata = data.latest('time')
        data = list()
        data.append(mydata)
        return super(FilteredMeasuredSerializer, self).to_representation(data)


class MeasuredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measured
        list_serializer_class = FilteredMeasuredSerializer
        fields = '__all__'


class MeasuredSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measured
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    measureds = MeasuredSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        fields = ['id', 'caseid', 'mode', 'autonomy', 'deleted', 'measureds']


class DeviceTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceTracking
        fields = '__all__'


class UserPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreference
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
