# Generated by Django 2.0.4 on 2018-04-27 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_order_db_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_db',
            name='user',
            field=models.CharField(max_length=30),
        ),
    ]
