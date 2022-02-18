# Generated by Django 3.1.5 on 2021-07-17 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor_engine', '0007_auto_20210715_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('levele_one', models.CharField(db_column='level_one', max_length=50)),
                ('level_two', models.CharField(db_column='level_two', max_length=50)),
                ('level_three', models.CharField(db_column='level_three', max_length=50)),
                ('level_four', models.CharField(db_column='level_four', max_length=50)),
                ('language', models.CharField(db_column='language', max_length=100)),
                ('isDarkMode', models.BooleanField(db_column='isDarkMode', default=False)),
            ],
            options={
                'db_table': 'tb_user_preference',
            },
        ),
    ]
