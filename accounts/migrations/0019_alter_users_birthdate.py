# Generated by Django 4.1.7 on 2023-03-17 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_users_email_alter_users_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='BirthDate',
            field=models.DateTimeField(blank=True, max_length=12, null=True),
        ),
    ]