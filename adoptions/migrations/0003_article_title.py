# Generated by Django 3.0 on 2020-10-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0002_auto_20201002_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
