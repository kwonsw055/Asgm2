# Generated by Django 2.1.2 on 2018-11-15 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='pw',
            field=models.CharField(default='', max_length=20),
        ),
    ]
