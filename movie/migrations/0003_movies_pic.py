# Generated by Django 3.0.6 on 2020-05-15 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20200515_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='pic',
            field=models.TextField(default='https://www.prokerala.com/movies/assets/img/no-poster-available.jpg', max_length=500),
        ),
    ]
