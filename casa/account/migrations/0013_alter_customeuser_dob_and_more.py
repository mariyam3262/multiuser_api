# Generated by Django 4.0.5 on 2022-07-26 09:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_dealerprofileadditional_marital_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeuser',
            name='dob',
            field=models.DateField(default=datetime.date(2022, 7, 26), verbose_name='Date Of Birth'),
        ),
        migrations.AlterField(
            model_name='marketingpersonadditional',
            name='joining_date',
            field=models.DateField(default=datetime.date(2022, 7, 26), verbose_name='joining Date'),
        ),
    ]