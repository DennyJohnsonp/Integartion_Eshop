# Generated by Django 3.2.3 on 2021-06-08 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_customer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='customer',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
