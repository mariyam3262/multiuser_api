# Generated by Django 4.0.3 on 2022-07-27 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_ordergeneration_price_ind_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordergeneration',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]