# Generated by Django 3.0.3 on 2020-06-29 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0031_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='p1',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='p2',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='p3',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
