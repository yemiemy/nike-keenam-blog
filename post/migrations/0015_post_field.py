# Generated by Django 2.2.2 on 2019-06-22 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='field',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
