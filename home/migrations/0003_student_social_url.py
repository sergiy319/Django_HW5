# Generated by Django 3.1.3 on 2020-12-20 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201207_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='social_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
