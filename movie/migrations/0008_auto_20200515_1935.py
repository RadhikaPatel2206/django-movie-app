# Generated by Django 3.0.6 on 2020-05-15 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20200515_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='pic',
            field=models.URLField(blank=True, default='https://www.prokerala.com/movies/assets/img/no-poster-available.jpg', max_length=500, null=True),
        ),
    ]
