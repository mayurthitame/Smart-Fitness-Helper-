# Generated by Django 2.2.13 on 2022-01-18 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendPlanadmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=50, null=True)),
                ('amount', models.CharField(max_length=10, null=True)),
                ('duration', models.CharField(max_length=10, null=True)),
                ('planN', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
