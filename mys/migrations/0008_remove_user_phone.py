# Generated by Django 5.1.1 on 2024-11-06 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mys', '0007_alter_user_preferred_colores_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]
