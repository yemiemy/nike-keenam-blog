# Generated by Django 2.2.2 on 2019-06-20 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_post_slide_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slide_image',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
    ]
