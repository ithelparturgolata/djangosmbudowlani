# Generated by Django 4.2.7 on 2023-12-17 08:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_pliki'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kalendarium',
            name='opis',
            field=ckeditor.fields.RichTextField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='pliki',
            name='opis',
            field=ckeditor.fields.RichTextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='przetargi',
            name='opis',
            field=ckeditor.fields.RichTextField(max_length=8000),
        ),
    ]