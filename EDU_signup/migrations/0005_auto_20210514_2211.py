# Generated by Django 3.1.5 on 2021-05-14 17:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EDU_signup', '0004_auto_20210514_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='mybaseuser',
            name='is_good_to_go',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mybaseuser',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
