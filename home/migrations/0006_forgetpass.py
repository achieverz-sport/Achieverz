# Generated by Django 3.1.1 on 2020-09-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200924_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='forgetpass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20)),
                ('key', models.CharField(max_length=20)),
            ],
        ),
    ]