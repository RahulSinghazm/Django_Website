# Generated by Django 2.0.7 on 2018-09-21 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=30)),
                ('experience_reqiured', models.IntegerField(default='0')),
                ('req_skills', models.CharField(default='skills required', max_length=100)),
                ('job_description', models.TextField(max_length=5000, null=True)),
                ('contact_no', models.CharField(default='0000000', max_length=10)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('job_id', models.CharField(default=0, max_length=8)),
                ('job_location', models.CharField(default='location', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.CharField(max_length=1000)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
