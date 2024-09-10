# Generated by Django 5.0.6 on 2024-08-30 11:45

import django.db.models.deletion
import store.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_remove_product_original_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Heritage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0=default, 1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default, 1=Trending')),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_keywords', models.CharField(max_length=150)),
                ('meta_description', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='original_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='selling_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='small_description',
            field=models.CharField(default='desc', max_length=250),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Heri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path)),
                ('small_description', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0=default, 1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default, 1=Trending')),
                ('tag', models.CharField(max_length=150)),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_keywords', models.CharField(max_length=150)),
                ('meta_description', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('heritage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.heritage')),
            ],
        ),
        migrations.DeleteModel(
            name='TraditionItem',
        ),
        migrations.DeleteModel(
            name='Traditions',
        ),
    ]