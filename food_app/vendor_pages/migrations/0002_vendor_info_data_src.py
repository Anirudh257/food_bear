# Generated by Django 2.0.4 on 2018-04-16 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor_info',
            name='data_src',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
