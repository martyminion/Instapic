# Generated by Django 3.0.6 on 2020-05-31 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0009_auto_20200531_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, to='photos.Profile'),
        ),
    ]