# Generated by Django 5.0.2 on 2024-02-15 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0008_alter_cacheduser_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cacheduser',
            name='last_login',
            field=models.DateTimeField(null=True),
        ),
    ]
