# Generated by Django 5.0.1 on 2024-01-16 07:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_mark_is_selected_mark_likes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='usersuggestion',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mark',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post', to=settings.AUTH_USER_MODEL),
        ),
    ]
