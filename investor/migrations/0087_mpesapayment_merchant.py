# Generated by Django 4.2.9 on 2024-07-12 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0086_remove_mpesarequest_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mpesapayment',
            name='merchant',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
