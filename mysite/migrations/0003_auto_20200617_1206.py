# Generated by Django 3.0.3 on 2020-06-17 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20200616_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
