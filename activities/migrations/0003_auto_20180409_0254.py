# Generated by Django 2.0.4 on 2018-04-09 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20180409_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='notes',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
