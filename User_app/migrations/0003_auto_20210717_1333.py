# Generated by Django 3.2.5 on 2021-07-17 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_app', '0002_auto_20210717_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
