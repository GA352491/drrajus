# Generated by Django 3.1.3 on 2021-03-22 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0011_agteam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agteam',
            name='pic',
            field=models.ImageField(upload_to='AG'),
        ),
    ]