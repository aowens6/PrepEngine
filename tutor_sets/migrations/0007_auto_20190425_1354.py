# Generated by Django 2.1 on 2019-04-25 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_sets', '0006_auto_20190424_1501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['order']},
        ),
        migrations.RenameField(
            model_name='option',
            old_name='questionId',
            new_name='question',
        ),
        migrations.RemoveField(
            model_name='option',
            name='option',
        ),
        migrations.AddField(
            model_name='option',
            name='text',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='question',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]