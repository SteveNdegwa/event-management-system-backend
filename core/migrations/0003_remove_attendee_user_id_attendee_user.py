# Generated by Django 5.0.2 on 2024-02-24 11:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_role_role_event'),
        ('user_management', '0013_alter_cacheduser_date_joined_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendee',
            name='user_id',
        ),
        migrations.AddField(
            model_name='attendee',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_management.cacheduser'),
        ),
    ]
