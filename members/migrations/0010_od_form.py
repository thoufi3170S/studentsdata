# Generated by Django 4.2.6 on 2024-03-30 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_destinaton_alter_member_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='od_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('idno', models.CharField(max_length=254)),
                ('Department_name', models.CharField(max_length=254)),
                ('type_of_od', models.CharField(max_length=254)),
                ('Reason', models.CharField(max_length=254)),
                ('Duration', models.CharField(max_length=254)),
                ('class_incharge_name', models.CharField(max_length=254)),
                ('staff_id', models.CharField(max_length=254)),
            ],
        ),
    ]
