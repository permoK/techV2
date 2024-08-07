# Generated by Django 4.2.9 on 2024-07-11 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0084_mpesarequest_delete_mpesatransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpesarequest',
            name='merchant',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='mpesarequest',
            name='phone_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mpesarequest',
            name='status',
            field=models.CharField(default='PENDING', max_length=100),
        ),
        migrations.AlterField(
            model_name='mpesarequest',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
