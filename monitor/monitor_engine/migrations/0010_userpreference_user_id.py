# Generated by Django 3.1.5 on 2021-07-17 04:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('monitor_engine', '0009_auto_20210717_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpreference',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
