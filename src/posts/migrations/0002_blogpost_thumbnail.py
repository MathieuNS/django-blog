# Generated by Django 5.1 on 2024-08-16 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='thumbnail',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
