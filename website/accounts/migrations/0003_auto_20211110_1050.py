# Generated by Django 3.2.7 on 2021-11-10 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_flag_scoreboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flag',
            name='description',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='flag',
            name='name',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]