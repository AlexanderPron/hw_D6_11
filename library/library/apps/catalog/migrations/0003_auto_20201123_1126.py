# Generated by Django 3.1.3 on 2020-11-23 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20201112_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Издательство')),
            ],
            options={
                'verbose_name': 'Издательство',
                'verbose_name_plural': 'Издательства',
            },
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
        migrations.AlterField(
            model_name='author',
            name='birth_year',
            field=models.SmallIntegerField(verbose_name='год рождения'),
        ),
        migrations.AlterField(
            model_name='author',
            name='country',
            field=models.CharField(max_length=2, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.TextField(verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(max_length=13, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='copy_count',
            field=models.SmallIntegerField(default=1, verbose_name='Копий'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.TextField(verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year_release',
            field=models.SmallIntegerField(verbose_name='Год издания'),
        ),
        migrations.AddField(
            model_name='book',
            name='ph_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.publishinghouse', verbose_name='Издательство'),
        ),
    ]