# Generated by Django 3.0.6 on 2020-11-03 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20201103_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='music.Album'),
        ),
    ]