# Generated by Django 4.1.7 on 2023-03-16 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_users_repeatpassword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='Email',
            field=models.TextField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='Password',
            field=models.CharField(max_length=50),
        ),
    ]
