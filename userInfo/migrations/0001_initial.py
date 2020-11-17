# Generated by Django 3.1.3 on 2020-11-13 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wxuser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('openid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=50)),
                ('avatar', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('creat_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
