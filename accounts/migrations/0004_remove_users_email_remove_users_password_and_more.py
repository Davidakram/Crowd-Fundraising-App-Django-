# Generated by Django 4.1.7 on 2023-03-11 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_users_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='users',
            name='Password',
        ),
        migrations.RemoveField(
            model_name='users',
            name='RepeatPassword',
        ),
        migrations.RemoveField(
            model_name='users',
            name='image',
        ),
        migrations.RemoveField(
            model_name='users',
            name='mobile_phone',
        ),
    ]