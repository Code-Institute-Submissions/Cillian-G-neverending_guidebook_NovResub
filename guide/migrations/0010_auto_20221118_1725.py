# Generated by Django 3.2.15 on 2022-11-18 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0009_auto_20220917_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='region',
        ),
        migrations.DeleteModel(
            name='BookmarkNotes',
        ),
    ]