# Generated by Django 3.0.4 on 2020-04-01 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teerresults', '0002_auto_20200331_0646'),
    ]

    operations = [
        migrations.CreateModel(
            name='DreamNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dream', models.CharField(max_length=32)),
                ('num', models.CharField(max_length=16)),
                ('house', models.CharField(max_length=16)),
                ('ending', models.CharField(max_length=16)),
            ],
        ),
    ]
