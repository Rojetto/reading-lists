# Generated by Django 4.1.4 on 2022-12-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_booklink'),
    ]

    operations = [
        migrations.AddField(
            model_name='booklink',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
