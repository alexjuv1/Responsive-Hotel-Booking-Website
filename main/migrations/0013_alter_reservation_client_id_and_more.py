# Generated by Django 4.1.3 on 2022-12-02 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0012_delete_admin_remove_testmod_user_id_delete_history_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.room'),
        ),
    ]
