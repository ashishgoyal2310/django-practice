# Generated by Django 3.0.4 on 2020-04-01 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teerresults', '0004_auto_20200401_0718'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title1', models.IntegerField()),
                ('title2', models.IntegerField()),
            ],
        ),
    ]
