# Generated by Django 3.2.6 on 2022-03-16 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0028_auto_20220316_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='localproduct',
            name='actualPrice',
            field=models.IntegerField(default=1),
        ),
    ]
