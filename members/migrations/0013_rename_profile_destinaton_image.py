# Generated by Django 5.1.4 on 2025-02-04 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0012_rename_department_name_od_form_department_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destinaton',
            old_name='profile',
            new_name='image',
        ),
    ]
