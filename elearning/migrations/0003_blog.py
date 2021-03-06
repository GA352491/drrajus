# Generated by Django 3.1.3 on 2021-02-17 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0002_auto_20201103_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('overview', models.TextField(blank=True, max_length=400, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.ImageField(upload_to='Blog')),
            ],
        ),
    ]
