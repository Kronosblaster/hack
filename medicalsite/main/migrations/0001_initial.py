# Generated by Django 4.0 on 2022-01-29 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medical_entries',
            fields=[
                ('job_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('descripton', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('posted_on', models.DateField()),
            ],
        ),
    ]