# Generated by Django 3.1.7 on 2021-10-03 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restbee_app', '0004_auto_20211003_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Errors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('error', models.CharField(blank=True, default='No registrado', max_length=255)),
            ],
        ),
    ]
