# Generated by Django 3.1.1 on 2020-09-23 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='other_fields',
        ),
        migrations.RemoveField(
            model_name='team',
            name='category',
        ),
        migrations.AddField(
            model_name='user',
            name='is_coach',
            field=models.BooleanField(default=False, verbose_name='Coach'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_group_manager',
            field=models.BooleanField(default=False, verbose_name='Group Manager'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(default=False, verbose_name='Manager'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_player',
            field=models.BooleanField(default=True, verbose_name='Player'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_referee',
            field=models.BooleanField(default=False, verbose_name='Referee'),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='Email Address')),
                ('mobile', models.CharField(max_length=15, unique=True, verbose_name='Mobile Number')),
                ('category', models.JSONField(default=list)),
                ('is_organizer', models.BooleanField(default=False, verbose_name='Organizer')),
                ('is_brand', models.BooleanField(default=False, verbose_name='Brand')),
                ('is_team', models.BooleanField(default=False, verbose_name='Team')),
                ('is_academy', models.BooleanField(default=False, verbose_name='Academy')),
                ('is_venue', models.BooleanField(default=False, verbose_name='Venue')),
                ('is_institute', models.BooleanField(default=False, verbose_name='Institute')),
                ('is_federation', models.BooleanField(default=False, verbose_name='Federation')),
                ('is_government', models.BooleanField(default=False, verbose_name='Government')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('additional', models.JSONField(default=dict)),
                ('address', models.ManyToManyField(blank=True, to='home.Address')),
                ('members', models.ManyToManyField(related_name='Group_Members', to=settings.AUTH_USER_MODEL)),
                ('primary_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.group'),
        ),
        migrations.DeleteModel(
            name='Organizer',
        ),
    ]
