# Generated by Django 3.1.5 on 2021-07-30 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor_engine', '0017_measured_autonomy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measured',
            name='autonomy',
        ),
        migrations.AddField(
            model_name='device',
            name='autonomy',
            field=models.CharField(db_column='autonomy', default=1, max_length=100),
            preserve_default=False,
        ),
    ]