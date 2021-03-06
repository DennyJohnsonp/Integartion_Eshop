# Generated by Django 3.1.6 on 2021-05-04 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('imgtitle', models.CharField(max_length=100)),
                ('imgdesc', models.CharField(max_length=600)),
                ('image', models.ImageField(upload_to='Images/')),
            ],
        ),
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgtitle', models.CharField(max_length=100)),
                ('imgdesc', models.CharField(max_length=600)),
                ('image', models.ImageField(upload_to='Images/category/ ')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Portfolio.categorie')),
            ],
        ),
    ]
