# Generated by Django 3.1.6 on 2021-05-08 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0003_auto_20210508_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='imgdesc',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='imgtitle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]