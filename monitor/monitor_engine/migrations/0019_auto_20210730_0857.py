# Generated by Django 3.1.5 on 2021-07-30 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor_engine', '0018_auto_20210730_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='autonomy',
            field=models.CharField(db_column='autonomy', default='0', max_length=100),
        ),
    ]
