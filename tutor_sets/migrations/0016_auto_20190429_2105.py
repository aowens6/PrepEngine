# Generated by Django 2.2 on 2019-04-29 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_sets', '0015_auto_20190429_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorset',
            name='score',
        ),
        migrations.RemoveField(
            model_name='tutorset',
            name='totalQuestions',
        ),
        migrations.AddField(
            model_name='tutorset',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
