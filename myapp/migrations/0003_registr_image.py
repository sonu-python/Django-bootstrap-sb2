# Generated by Django 2.2.3 on 2019-07-16 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_registr_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='registr',
            name='image',
            field=models.ImageField(default='', upload_to='pic_folder/'),
        ),
    ]