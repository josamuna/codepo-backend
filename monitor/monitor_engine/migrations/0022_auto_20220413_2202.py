# Generated by Django 3.2.12 on 2022-04-13 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor_engine', '0021_auto_20220222_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='autonomy',
        ),
        migrations.RemoveField(
            model_name='measured',
            name='soc',
        ),
        migrations.AddField(
            model_name='measured',
            name='energy_in',
            field=models.FloatField(db_column='energy_in', null=True),
        ),
        migrations.AddField(
            model_name='measured',
            name='energy_out',
            field=models.FloatField(db_column='energy_out', null=True),
        ),
        migrations.AddField(
            model_name='measured',
            name='temperature',
            field=models.FloatField(db_column='temperature', null=True),
        ),
        migrations.AlterField(
            model_name='measured',
            name='latitude',
            field=models.FloatField(db_column='latitude', null=True),
        ),
        migrations.AlterField(
            model_name='measured',
            name='longitude',
            field=models.FloatField(db_column='longitude', null=True),
        ),
    ]
