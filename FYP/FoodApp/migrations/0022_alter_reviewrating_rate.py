# Generated by Django 3.2.6 on 2022-02-23 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0021_alter_reviewrating_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='rate',
            field=models.IntegerField(default=1),
        ),
    ]
