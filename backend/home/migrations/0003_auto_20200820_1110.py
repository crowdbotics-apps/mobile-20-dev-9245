# Generated by Django 2.2.15 on 2020-08-20 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_load_initial_data"),
    ]

    operations = [
        migrations.RemoveField(model_name="homepage", name="body",),
        migrations.AddField(
            model_name="homepage", name="body12345", field=models.TextField(blank=True),
        ),
    ]
