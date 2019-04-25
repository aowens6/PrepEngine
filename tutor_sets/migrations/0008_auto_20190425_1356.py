# Generated by Django 2.1 on 2019-04-25 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_sets', '0007_auto_20190425_1354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='option',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='option',
            name='correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='option',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
