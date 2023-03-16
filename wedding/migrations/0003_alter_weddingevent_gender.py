# Generated by Django 4.1.7 on 2023-03-15 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0002_alter_weddingevent_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weddingevent',
            name='gender',
            field=models.CharField(choices=[('D', 'GENDER_CHOICES'), ('Bride', ' Bride'), ('Groom', ' Groom')], default='D', max_length=10),
        ),
    ]
