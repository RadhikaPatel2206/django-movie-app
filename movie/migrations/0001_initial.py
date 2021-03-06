# Generated by Django 3.0.6 on 2020-05-15 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('movie', models.CharField(max_length=100)),
                ('desc', models.CharField(blank=True, max_length=500, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('added_date', models.DateTimeField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
