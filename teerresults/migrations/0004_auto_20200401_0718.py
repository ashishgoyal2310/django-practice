# Generated by Django 3.0.4 on 2020-04-01 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teerresults', '0003_dreamnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dreamnumber',
            name='ending',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='dreamnumber',
            name='house',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='dreamnumber',
            name='num',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]
