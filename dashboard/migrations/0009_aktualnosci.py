# Generated by Django 4.2.7 on 2023-12-17 10:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_kalendarium_opis_alter_pliki_opis_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aktualnosci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_utworzenia', models.DateTimeField(auto_now_add=True)),
                ('tytul', models.CharField(max_length=255)),
                ('opis', ckeditor.fields.RichTextField(max_length=8000)),
                ('grafika', models.ImageField(upload_to='aktualnosci/')),
            ],
        ),
    ]