# Generated by Django 3.0.3 on 2020-06-19 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0016_auto_20200619_2121'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]