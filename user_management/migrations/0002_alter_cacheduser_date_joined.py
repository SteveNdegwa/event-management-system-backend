# Generated by Django 5.0.2 on 2024-02-12 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cacheduser',
            name='date_joined',
            field=models.DateTimeField(editable=False),
        ),
    ]
