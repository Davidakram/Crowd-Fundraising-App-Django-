# Generated by Django 4.1.7 on 2023-03-15 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaignapp', '0003_user_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]