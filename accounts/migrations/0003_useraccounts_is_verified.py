# Generated by Django 3.1.6 on 2021-02-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_friends_profilepicture'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccounts',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
