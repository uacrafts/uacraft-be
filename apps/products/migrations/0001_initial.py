# Generated by Django 5.0.6 on 2024-06-19 11:52

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата Створення')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата Оновлення')),
                ('title', models.CharField(default='Без бренду', max_length=100, unique=True, verbose_name='Назва бренду')),
                ('logo', models.ImageField(upload_to='logos/', verbose_name='Логотип бренду')),
                ('description', models.TextField(blank=True, verbose_name='Опис бренду')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренди',
                'db_table': 'product_brand',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regular_price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0, message='Must be greater than or equal to 0.0.')], verbose_name='Звичайна ціна')),
                ('special_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0, message='Must be greater than or equal to 0.0.')], verbose_name='Ціна зі знижкою')),
                ('discount_percentage', models.DecimalField(decimal_places=1, default=0.0, max_digits=10, verbose_name='Відсоток знижки')),
            ],
            options={
                'verbose_name': 'Ціна',
                'verbose_name_plural': 'Ціни',
                'db_table': 'product_price',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата Створення')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата Оновлення')),
                ('title', models.CharField(max_length=255, verbose_name='Назва продавця')),
                ('city', models.CharField(max_length=255, verbose_name='Місто')),
                ('is_displayed', models.BooleanField(choices=[(False, 'Деактивовано'), (True, 'Активовано')], db_index=True, default=1, verbose_name='Статус')),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Продавець',
                'verbose_name_plural': 'Продавці',
                'db_table': 'product_store',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата Створення')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата Оновлення')),
                ('title', models.CharField(max_length=100, verbose_name='Назва категорії')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.category', verbose_name='Батьківська категорія')),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
                'db_table': 'product_category',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата Створення')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата Оновлення')),
                ('title', models.CharField(max_length=255, verbose_name='Назва продукту')),
                ('quantity_in_stock', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0, message='Must be greater than or equal to 0.')], verbose_name='Кількість товарів')),
                ('description', models.TextField(blank=True, verbose_name='Опис товару')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brand_products', to='products.brand', verbose_name='Назва бренду')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category_products', to='products.category', verbose_name='Категорія')),
                ('price', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.price', verbose_name='Ціна')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_sellers', to='products.seller', verbose_name='Продавець')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукти',
                'db_table': 'product',
                'ordering': (models.Case(models.When(price__special_price__gt=0, then='price__special_price'), default='price__regular_price'), 'price__regular_price'),
                'unique_together': {('title', 'seller')},
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Фото')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='products.product')),
            ],
            options={
                'verbose_name': 'Фото продукта',
                'verbose_name_plural': 'Фото продуктів',
                'db_table': 'product_image',
            },
        ),
    ]
