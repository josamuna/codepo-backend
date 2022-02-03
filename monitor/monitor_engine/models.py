from django.contrib.auth.models import User
from django.db import models


class Device(models.Model):
    caseid = models.CharField(max_length=255, db_column="caseid")
    mode = models.CharField(max_length=255, db_column="mode")
    interval_bat_s = models.FloatField(db_column="interval_bat_s", null=True)
    interval_sending_h = models.FloatField(db_column="interval_sending_h", null=True)
    total_capacity = models.IntegerField(db_column='total_capacity', null=True, default=0)
    autonomy = models.CharField(db_column="autonomy", max_length=100, default="0")
    deleted = models.BooleanField(db_column="deleted", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(db_column='created_by', default=0)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(db_column='updated_by', default=0)
    deleted_at = models.DateTimeField(null=True)
    deleted_by = models.IntegerField(db_column='deleted_by', default=0)

    class Meta:
        db_table = 'tb_device'

    def __str__(self):
        return self.caseid


class Measured(models.Model):
    latitude = models.FloatField(db_column="latitude")
    longitude = models.FloatField(db_column="longitude")
    # source = models.CharField(max_length=255, db_column="source")
    soc = models.FloatField(db_column="soc")
    time = models.DateTimeField(db_column="time", auto_now=True)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE, db_column="device_id", related_name='measureds')

    class Meta:
        db_table = 'tb_measured'


# class DeviceMeasures(models.Model):
#     device_id = models.ForeignKey(Device, on_delete = models.CASCADE)
#     measures_id = models.ForeignKey(Measured, on_delete = models.CASCADE)

#     class Meta:
#         db_table = 'tb_device_measures'

class Command(models.Model):
    command = models.CharField(max_length=255, db_column='command')
    description = models.CharField(max_length=255, db_column='description')
    deleted = models.BooleanField(db_column="deleted", default=False)

    class Meta:
        db_table = 'tb_command'

    def __str__(self):
        return self.command


class DeviceTracking(models.Model):
    time = models.DateTimeField(auto_now_add=True, db_column='time')
    isTrack = models.BooleanField(db_column='isTrack')
    user_id = models.ForeignKey(User, db_column='user_id', on_delete=models.CASCADE)
    device_id = models.ForeignKey(Device, db_column='device_id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_device_tracking'


class CommandHistory(models.Model):
    time = models.DateTimeField(auto_now_add=True, db_column='time')
    mode = models.CharField(max_length=100, db_column='mode')
    interval_bat = models.IntegerField(db_column='interval_bat')
    interval_send = models.IntegerField(db_column='interval_send')
    user_id = models.ForeignKey(User, db_column='user_id', on_delete=models.CASCADE)
    device_id = models.ForeignKey(Device, db_column='device_id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_command_history'


class UserPreference(models.Model):
    level_one = models.CharField(max_length=50, db_column='level_one', null=True)
    level_two = models.CharField(max_length=50, db_column='level_two', null=True)
    level_three = models.CharField(max_length=50, db_column='level_three', null=True)
    level_four = models.CharField(max_length=50, db_column='level_four', null=True)
    language = models.CharField(max_length=100, db_column='language', default='English')
    isDarkMode = models.BooleanField(default=False, db_column='isDarkMode')
    user_id = models.ForeignKey(User, db_column='user_id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_user_preference'


class Notification(models.Model):
    notification = models.CharField(max_length=500, db_column='notification')
    caseid = models.CharField(max_length=100, db_column='caseid')
    status = models.BooleanField(db_column='status', default=False)
    time = models.DateTimeField(db_column='time')
    device_id = models.ForeignKey(Device, db_column='device_id', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, db_column='user_id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tb_notification'

# class Mode(models.Model):
#     designation

# class Role(models.Model):
#     designation = models.CharField(max_length=200, db_column="designation")

#     class Meta:
#         db_table = 'tb_role'

#     def __str__(self):
#         return self.designation

# class UserRole(models.Model):
#     user_id = models.ForeignKey(User, on_delete = models.CASCADE)
#     role_id = models.ForeignKey(Role, on_delete = models.CASCADE)

#     class Meta:
#         db_table = 'tb_user_role'
