# Generated by Django 3.1.1 on 2020-09-24 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_verification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='verification',
            old_name='Email',
            new_name='email',
        ),
    ]