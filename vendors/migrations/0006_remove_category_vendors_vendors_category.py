# Generated by Django 4.1.7 on 2023-03-20 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0005_alter_category_vendors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='vendors',
        ),
        migrations.AddField(
            model_name='vendors',
            name='category',
            field=models.ManyToManyField(related_name='category_vendor', to='vendors.category'),
        ),
    ]
