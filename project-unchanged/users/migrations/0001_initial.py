# Generated by Django 3.1 on 2020-10-22 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('has_provided_billing_data', models.BooleanField(default=False)),
                ('has_provided_password', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('cedula', models.CharField(max_length=15, null=True, unique=True)),
                ('is_gas_station_admin', models.BooleanField(default=False)),
                ('city', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('devices', models.JSONField(null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VehiclesId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('alias', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles_ids', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('gas_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.gasstation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserGasStationBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField(default=0.0)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('gas_station', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.gasstation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]