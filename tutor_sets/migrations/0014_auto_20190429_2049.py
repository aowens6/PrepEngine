# Generated by Django 2.2 on 2019-04-29 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_sets', '0013_question_explanation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='option',
            options={},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={},
        ),
        migrations.RemoveField(
            model_name='option',
            name='order',
        ),
        migrations.RemoveField(
            model_name='question',
            name='order',
        ),
        migrations.RemoveField(
            model_name='question',
            name='shuffle_answers',
        ),
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