# Generated by Django 5.0.1 on 2024-01-07 04:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentregistration',
            old_name='city',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='studentregistration',
            name='roll',
        ),
        migrations.AddField(
            model_name='studentregistration',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
