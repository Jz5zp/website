# Generated by Django 3.0 on 2020-10-10 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0006_article_illustration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='illustration',
            field=models.ImageField(null=True, upload_to='images/illustration', verbose_name='picture'),
        ),
    ]
