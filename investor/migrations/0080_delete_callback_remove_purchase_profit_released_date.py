# Generated by Django 4.2.9 on 2024-07-07 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0079_purchase_profit_released_date_alter_callback_result'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Callback',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='profit_released_date',
        ),
    ]
