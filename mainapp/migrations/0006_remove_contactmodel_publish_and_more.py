# Generated by Django 4.0.5 on 2022-09-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_rename_lasttname_contactmodel_lastname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmodel',
            name='publish',
        ),
        migrations.AlterField(
            model_name='podcastmodel',
            name='category',
            field=models.ManyToManyField(related_name='pods', to='mainapp.podcastermodel'),
        ),
    ]
