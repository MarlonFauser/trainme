# Generated by Django 2.1.4 on 2018-12-10 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='classname',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]