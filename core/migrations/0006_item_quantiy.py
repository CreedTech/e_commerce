# Generated by Django 4.0.4 on 2022-05-18 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantiy',
            field=models.IntegerField(default=1),
        ),
    ]
