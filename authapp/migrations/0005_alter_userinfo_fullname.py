# Generated by Django 4.1.6 on 2023-09-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_userinfo_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='fullname',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]