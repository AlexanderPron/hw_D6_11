# Generated by Django 3.1.3 on 2020-12-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20201217_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_img',
            field=models.ImageField(blank=True, upload_to='book_pics/%Y/%m/%d'),
        ),
    ]