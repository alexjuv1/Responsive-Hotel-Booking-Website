# Generated by Django 4.1.3 on 2022-11-25 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_testmod'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmod',
            name='test1',
            field=models.CharField(default='NONE', max_length=200),
        ),
    ]