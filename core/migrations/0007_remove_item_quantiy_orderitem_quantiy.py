# Generated by Django 4.0.4 on 2022-05-18 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_item_quantiy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantiy',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantiy',
            field=models.IntegerField(default=1),
        ),
    ]
