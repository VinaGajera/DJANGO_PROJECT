# Generated by Django 3.2.4 on 2021-09-09 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='c_id',
            new_name='course',
        ),
    ]
