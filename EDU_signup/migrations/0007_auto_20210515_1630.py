# Generated by Django 3.1.5 on 2021-05-15 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDU_signup', '0006_auto_20210515_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybaseuser',
            name='two_factor_code',
            field=models.IntegerField(blank=True, max_length=10, null=True, verbose_name='کد رهگیری'),
        ),
    ]
