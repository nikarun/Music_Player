# Generated by Django 3.0.6 on 2020-11-03 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_song_song_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='composer',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='song',
            name='name',
        ),
    ]
