# Generated by Django 3.0.6 on 2020-05-31 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0010_auto_20200531_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='_profile_following_+', to='photos.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='_profile_followers_+', to='photos.Profile'),
        ),
    ]
