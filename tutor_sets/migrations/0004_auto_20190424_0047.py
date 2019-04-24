# Generated by Django 2.1 on 2019-04-24 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_sets', '0003_tutorset_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionText', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('tutorSetID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor_sets.TutorSet')),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='questionId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor_sets.Question'),
        ),
    ]
