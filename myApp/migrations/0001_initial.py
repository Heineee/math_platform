# Generated by Django 3.2.15 on 2024-09-14 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('identify', models.CharField(max_length=8, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'admin-account',
            },
        ),
        migrations.CreateModel(
            name='Posttext',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=1000)),
                ('username', models.CharField(max_length=20)),
                ('pictureaddress', models.CharField(blank=True, max_length=100, null=True)),
                ('index', models.AutoField(primary_key=True, serialize=False)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('recommended_developer', models.BooleanField(default=False)),
                ('viewers', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'text',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('last_exit', models.DateTimeField(auto_now=True)),
                ('pictureaddress', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'user-account',
            },
        ),
    ]