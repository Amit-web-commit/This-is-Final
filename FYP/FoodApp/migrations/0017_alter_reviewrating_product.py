# Generated by Django 3.2.6 on 2022-02-20 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0016_auto_20220220_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodApp.localproduct'),
        ),
    ]
