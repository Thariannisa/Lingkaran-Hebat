# Generated by Django 3.0.5 on 2020-06-05 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='no_hp',
        ),
        migrations.RemoveField(
            model_name='user',
            name='stnk',
        ),
        migrations.AddField(
            model_name='user',
            name='umur',
            field=models.IntegerField(blank=True, null=True, verbose_name='Umur'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/', verbose_name='Gambar'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email address'),
        ),
    ]
