# Generated by Django 3.0 on 2020-10-17 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0007_auto_20201011_0131'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='illustration',
            field=models.ImageField(upload_to='img', verbose_name='ill'),
        ),
    ]
