# Generated by Django 4.1.7 on 2023-03-16 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaignapp', '0007_alter_campaign_avg_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='is_Reported',
            field=models.BooleanField(default=False),
        ),
    ]
