# Generated by Django 2.0.4 on 2018-04-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0005_auto_20180409_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='notes',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]