# Generated by Django 3.2.7 on 2021-09-11 17:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_car_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='fuel_t',
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
