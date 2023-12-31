# Generated by Django 4.0 on 2023-02-04 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('symptoms', models.CharField(max_length=200)),
                ('severity', models.CharField(max_length=200)),
                ('option', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
            ],
        ),
    ]
