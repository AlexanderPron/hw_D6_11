# Generated by Django 3.1.3 on 2020-12-17 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20201204_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinuse',
            name='book_isbn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='books', to='catalog.book', verbose_name='Книга'),
        ),
        migrations.AlterField(
            model_name='bookinuse',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='friends', to='catalog.friend', verbose_name='Кто взял'),
        ),
    ]
