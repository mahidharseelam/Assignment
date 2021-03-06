# Generated by Django 2.1.4 on 2018-12-28 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_id', models.IntegerField()),
                ('college_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_id', models.IntegerField()),
                ('contest_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_id', models.IntegerField()),
                ('hacker_id', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Submission_Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_id', models.IntegerField()),
                ('total_submission', models.IntegerField()),
                ('total_accepted_submissions', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='View_Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_id', models.IntegerField()),
                ('total_views', models.IntegerField()),
                ('total_unique_views', models.IntegerField()),
            ],
        ),
    ]
