# Generated by Django 4.2.6 on 2023-11-14 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0002_rename_space_mobiles_specs_alter_mobiles_display'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobiles',
            name='pictures',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
