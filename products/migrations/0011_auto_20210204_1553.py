# Generated by Django 3.1.4 on 2021-02-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210204_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image_rear_check',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]