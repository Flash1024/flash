# Generated by Django 3.0.3 on 2020-06-23 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0023_auto_20200622_1134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=120, null=True)),
                ('project_link', models.URLField(blank=True, max_length=750)),
                ('project_thumbnail', models.ImageField(default='', upload_to='mysite/media/portfolio/images')),
                ('project_type', models.CharField(choices=[('web', 'Web'), ('app', 'App')], default='web', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(default='', upload_to='mysite/media/review/images'),
        ),
    ]
