# Generated by Django 4.1.7 on 2023-03-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaignapp', '0005_remove_rating_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
    ]
