# Generated by Django 3.0.6 on 2020-11-03 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_song_album_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='song',
            name='image',
        ),
        migrations.RemoveField(
            model_name='song',
            name='lyricists',
        ),
        migrations.RemoveField(
            model_name='song',
            name='song_url',
        ),
    ]
