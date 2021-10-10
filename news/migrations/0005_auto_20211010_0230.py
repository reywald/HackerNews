# Generated by Django 3.2.8 on 2021-10-10 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20211008_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='score',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='story',
            name='text',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
