# Generated by Django 3.2.3 on 2021-09-30 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myemp',
            name='phone',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
