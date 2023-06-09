# Generated by Django 4.1.7 on 2023-03-23 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendors', '0004_remove_vendors_id_alter_vendors_vendors_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendors',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vendors',
            name='vendors_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vendor', to=settings.AUTH_USER_MODEL),
        ),
    ]
