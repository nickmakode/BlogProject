# Generated by Django 3.2.5 on 2021-07-17 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
