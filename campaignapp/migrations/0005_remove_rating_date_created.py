# Generated by Django 4.1.7 on 2023-03-16 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaignapp', '0004_alter_campaign_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='date_created',
        ),
    ]
