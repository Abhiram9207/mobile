# Generated by Django 4.2.6 on 2023-11-03 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobiles',
            old_name='space',
            new_name='specs',
        ),
        migrations.AlterField(
            model_name='mobiles',
            name='display',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
