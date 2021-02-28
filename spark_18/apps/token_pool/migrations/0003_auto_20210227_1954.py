# Generated by Django 3.0 on 2021-02-27 19:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('token_pool', '0002_auto_20210227_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokenpool',
            name='expire_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tokenpool',
            name='token',
            field=models.CharField(default=uuid.UUID('71d22e1f-86f4-428e-bc69-ef4ef9539a7d'), max_length=200, verbose_name='token'),
        ),
    ]
