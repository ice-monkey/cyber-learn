# Generated by Django 3.2.7 on 2021-12-10 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20211210_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_flag',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]