# Generated by Django 5.2.1 on 2025-06-20 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tinoe_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
