# Generated by Django 4.2.5 on 2023-09-22 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0002_character_banned'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='blocked',
            field=models.BooleanField(default=False),
        ),
    ]
