# Generated by Django 4.0.3 on 2022-04-08 06:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spekar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('discption', ckeditor.fields.RichTextField()),
                ('location', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='')),
                ('spekars', models.ManyToManyField(to='events.spekar')),
            ],
        ),
    ]
