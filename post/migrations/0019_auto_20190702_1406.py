# Generated by Django 2.2.2 on 2019-07-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0018_auto_20190702_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
