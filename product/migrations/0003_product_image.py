# Generated by Django 4.0.2 on 2022-02-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_category_product_is_stock_product_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, height_field=100, null=True, upload_to='media/', width_field=100),
        ),
    ]
