# Generated by Django 3.0.3 on 2020-07-01 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0039_remove_contactinfo_map_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='contact_email',
            field=models.CharField(max_length=40),
        ),
    ]