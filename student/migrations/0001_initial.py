# Generated by Django 3.2 on 2021-04-23 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_code', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('sex', models.CharField(max_length=200)),
                ('grade', models.CharField(max_length=200)),
                ('marjo', models.CharField(max_length=200)),
            ],
        ),
    ]
