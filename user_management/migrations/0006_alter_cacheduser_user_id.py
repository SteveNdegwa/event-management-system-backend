# Generated by Django 5.0.2 on 2024-02-13 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0005_alter_cacheduser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cacheduser',
            name='user_id',
            field=models.CharField(max_length=255),
        ),
    ]
