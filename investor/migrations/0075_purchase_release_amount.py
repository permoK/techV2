# Generated by Django 4.2.10 on 2024-04-02 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0074_purchase_profit_alter_item_name_alter_item_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='release_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
