# Generated by Django 5.1.6 on 2025-03-31 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_patient_contact_info'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Chat',
        ),
    ]
