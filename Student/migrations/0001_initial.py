# Generated by Django 3.2.4 on 2021-07-19 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('contact', models.PositiveIntegerField(max_length=12)),
                ('city', models.CharField(max_length=40)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=8)),
                ('profile_photo', models.ImageField(upload_to='profile_pic/')),
            ],
        ),
    ]