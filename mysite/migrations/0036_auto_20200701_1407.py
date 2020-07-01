# Generated by Django 3.0.3 on 2020-07-01 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0035_contactinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='contact_address',
        ),
        migrations.RemoveField(
            model_name='contactinfo',
            name='website',
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='contact_location',
            field=models.TextField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='contact_email',
            field=models.URLField(),
        ),
    ]
