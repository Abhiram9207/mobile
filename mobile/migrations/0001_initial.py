# Generated by Django 4.2.6 on 2023-11-03 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mobiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('price', models.PositiveIntegerField()),
                ('brand', models.CharField(max_length=200)),
                ('space', models.CharField(max_length=200)),
                ('display', models.CharField(max_length=200)),
            ],
        ),
    ]
