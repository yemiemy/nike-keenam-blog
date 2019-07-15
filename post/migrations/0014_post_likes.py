# Generated by Django 2.2.2 on 2019-06-21 21:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0013_message_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(default=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
