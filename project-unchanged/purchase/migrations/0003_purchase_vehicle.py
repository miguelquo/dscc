# Generated by Django 3.1 on 2020-10-30 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('purchase', '0002_auto_20201022_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.vehiclesid'),
        ),
    ]
