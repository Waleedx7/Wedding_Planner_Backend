# Generated by Django 4.1.7 on 2023-03-18 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0004_alter_weddingevent_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weddingevent',
            name='budget',
            field=models.PositiveIntegerField(),
        ),
    ]