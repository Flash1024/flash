# Generated by Django 3.0.3 on 2020-07-01 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0036_auto_20200701_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
