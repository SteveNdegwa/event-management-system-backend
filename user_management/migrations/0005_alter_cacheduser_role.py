# Generated by Django 5.0.2 on 2024-02-13 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0004_cacheduser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cacheduser',
            name='role',
            field=models.CharField(max_length=255),
        ),
    ]