# Generated by Django 5.0.2 on 2024-02-29 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.TextField(null=True),
        ),
    ]
