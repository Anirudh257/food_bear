# Generated by Django 2.0.4 on 2018-04-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_pages', '0010_auto_20180420_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor_info',
            name='food_items',
            field=models.CharField(default='wwe', max_length=255),
            preserve_default=False,
        ),
    ]