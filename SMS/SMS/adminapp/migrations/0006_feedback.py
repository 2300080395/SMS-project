# Generated by Django 5.0.7 on 2024-10-16 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('mobileno', models.CharField(max_length=10)),
                ('feedback', models.CharField(max_length=150)),
            ],
        ),
    ]
