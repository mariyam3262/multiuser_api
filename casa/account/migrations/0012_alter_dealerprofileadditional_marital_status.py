# Generated by Django 4.0.5 on 2022-07-14 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_dealerprofileadditional_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealerprofileadditional',
            name='marital_status',
            field=models.CharField(choices=[('Married', 'Married'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('Divorced', 'Divorced'), ('Single', 'Single')], default=None, max_length=9, null=True, verbose_name='Marital Status'),
        ),
    ]
