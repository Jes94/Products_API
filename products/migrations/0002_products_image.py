# Generated by Django 4.0.4 on 2022-04-13 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.CharField(default='empty', max_length=255),
        ),
    ]
