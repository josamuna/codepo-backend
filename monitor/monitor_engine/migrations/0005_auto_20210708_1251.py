# Generated by Django 3.1.5 on 2021-07-08 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor_engine', '0004_auto_20210708_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
