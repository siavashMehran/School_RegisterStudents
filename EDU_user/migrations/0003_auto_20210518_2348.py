# Generated by Django 3.1.5 on 2021-05-18 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDU_user', '0002_auto_20210518_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_auth_state',
            name='stu_birthday',
            field=models.CharField(blank=True, max_length=12, verbose_name='تاریخ تولد'),
        ),
    ]
