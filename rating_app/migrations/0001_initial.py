# Generated by Django 3.0.6 on 2020-05-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='credited_courses_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=15)),
                ('faculty_name', models.CharField(max_length=50)),
                ('course_name', models.CharField(max_length=50)),
                ('feedback_status', models.BooleanField()),
            ],
            options={
                'db_table': 'credited_courses_table',
            },
        ),
        migrations.CreateModel(
            name='rating_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=50)),
                ('course_name', models.CharField(max_length=50)),
                ('question_1', models.IntegerField()),
                ('question_2', models.IntegerField()),
                ('question_3', models.IntegerField()),
                ('question_4', models.IntegerField()),
                ('question_5', models.IntegerField()),
                ('question_6', models.IntegerField()),
                ('question_7', models.IntegerField()),
                ('count', models.IntegerField()),
            ],
            options={
                'db_table': 'rating_table',
            },
        ),
    ]
