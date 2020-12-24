# Generated by Django 3.1.4 on 2020-12-24 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('brand', models.CharField(max_length=254)),
                ('name', models.CharField(max_length=254)),
                ('release', models.CharField(max_length=254)),
                ('size', models.CharField(max_length=254)),
                ('os', models.CharField(max_length=254)),
                ('screen_size', models.CharField(max_length=254)),
                ('resolution', models.CharField(max_length=254)),
                ('number_of_cams', models.IntegerField()),
                ('camera_1', models.CharField(max_length=254)),
                ('camera_2', models.CharField(max_length=254)),
                ('camera_3', models.CharField(max_length=254)),
                ('picture', models.CharField(max_length=254)),
                ('video', models.CharField(max_length=254)),
                ('ram', models.CharField(max_length=254)),
                ('card_reader', models.CharField(max_length=254)),
                ('card_supported', models.CharField(max_length=254)),
                ('storage_cap', models.CharField(max_length=254)),
                ('microphone', models.BooleanField(blank=True, default=False, null=True)),
                ('speakers', models.BooleanField(blank=True, default=False, null=True)),
                ('headphone_jack', models.BooleanField(blank=True, default=False, null=True)),
                ('wireless_charging', models.BooleanField(blank=True, default=False, null=True)),
                ('charging_port', models.CharField(max_length=254)),
                ('battery', models.CharField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
    ]
