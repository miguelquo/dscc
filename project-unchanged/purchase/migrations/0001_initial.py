# Generated by Django 3.1 on 2020-10-22 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price_per_gallon', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('since_date', models.DateTimeField()),
                ('is_current', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField()),
                ('gallons', models.FloatField(null=True)),
                ('qrcode_string', models.CharField(max_length=1000)),
                ('number_code', models.CharField(max_length=100)),
                ('code_expiry_date', models.DateTimeField()),
                ('id_done', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseFuelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(default=0)),
                ('comment', models.CharField(max_length=1000)),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='purchase.purchase')),
            ],
        ),
    ]
