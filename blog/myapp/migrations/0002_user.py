# Generated by Django 3.0.2 on 2020-02-23 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]