# Generated by Django 3.1.5 on 2021-06-07 21:45

import EDU_user.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EDU_user', '0003_auto_20210518_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_auth_state',
            name='stu_paye',
            field=models.CharField(choices=[('fourth', 'چهارم'), ('fifth', 'پنجم'), ('sixth', 'ششم'), (None, 'انتخاب پایه')], max_length=15, verbose_name='پایه مورد نظر'),
        ),
        migrations.CreateModel(
            name='User_Upload_Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_student', models.FileField(upload_to=EDU_user.models.media_upload_path, verbose_name='اسکن شناسنامه مادر')),
                ('scan_mom', models.FileField(upload_to=EDU_user.models.media_upload_path, verbose_name='اسکن شناسنامه مادر')),
                ('scan_dad', models.FileField(upload_to=EDU_user.models.media_upload_path, verbose_name='اسکن شناسنامه پدر')),
                ('scan_lease', models.FileField(upload_to=EDU_user.models.media_upload_path, verbose_name='اسکن سند یا قولنامه محل زندگی')),
                ('scan_karname', models.FileField(upload_to=EDU_user.models.media_upload_path, verbose_name='اسکن کارنامه آخر')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
