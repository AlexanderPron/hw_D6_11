# Generated by Django 3.1.3 on 2020-12-03 21:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20201204_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinuse',
            name='start_use_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата выдачи'),
        ),
    ]
