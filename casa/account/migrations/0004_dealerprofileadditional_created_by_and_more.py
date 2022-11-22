# Generated by Django 4.0.5 on 2022-07-14 08:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_customeuser_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealerprofileadditional',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customeuser',
            name='dob',
            field=models.DateField(default=datetime.date(2022, 7, 14), verbose_name='Date Of Birth'),
        ),
    ]