# Generated by Django 2.2.6 on 2019-12-01 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20191201_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]