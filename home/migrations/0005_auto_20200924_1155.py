# Generated by Django 3.1.1 on 2020-09-24 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200924_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='email',
            field=models.CharField(max_length=20),
        ),
    ]