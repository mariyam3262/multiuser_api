# Generated by Django 4.0.5 on 2022-07-21 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.CharField(max_length=200)),
                ('pdf', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Surface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surface', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Thickness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thickness', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, null=True)),
                ('weight', models.CharField(max_length=200)),
                ('product_image', models.ImageField(upload_to='')),
                ('preview', models.ImageField(max_length=30, upload_to='')),
                ('is_deleted', models.BooleanField(default=False)),
                ('product_quantity', models.IntegerField(default=0)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.collection')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.size')),
                ('surface', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.surface')),
                ('thickness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.thickness')),
            ],
        ),
        migrations.CreateModel(
            name='OrderGeneration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField()),
                ('order_time', models.TimeField()),
                ('order_total_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_total_box', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
