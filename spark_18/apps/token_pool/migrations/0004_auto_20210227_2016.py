# Generated by Django 3.0 on 2021-02-27 20:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('token_pool', '0003_auto_20210227_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokenpool',
            name='token',
            field=models.CharField(default=uuid.UUID('3aa7e4a2-b1e0-47e9-aa69-406f40f7b81a'), max_length=200, verbose_name='token'),
        ),
    ]
