# Generated by Django 3.2.6 on 2022-02-08 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0011_rename_teamprofile_localproduct_localproductimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialProductimage', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
