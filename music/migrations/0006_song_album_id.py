# Generated by Django 3.0.6 on 2020-11-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20201103_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album_id',
            field=models.IntegerField(null=True),
        ),
    ]
