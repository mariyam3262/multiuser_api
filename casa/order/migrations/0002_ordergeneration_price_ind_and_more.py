# Generated by Django 4.0.5 on 2022-07-21 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordergeneration',
            name='price_ind',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ordergeneration',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]