# Generated by Django 3.2.6 on 2022-04-02 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0036_auto_20220402_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservetable',
            name='person',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='reservetable',
            name='selecthour',
            field=models.CharField(max_length=50),
        ),
    ]
