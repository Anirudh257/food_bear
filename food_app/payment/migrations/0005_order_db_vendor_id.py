# Generated by Django 2.0.4 on 2018-04-27 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20180427_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_db',
            name='vendor_id',
            field=models.CharField(default='N/A', max_length=30),
        ),
    ]
