# Generated by Django 3.2.6 on 2022-04-02 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FoodApp', '0037_auto_20220402_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservetable',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
