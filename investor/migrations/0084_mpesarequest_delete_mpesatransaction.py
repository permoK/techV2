# Generated by Django 4.2.9 on 2024-07-11 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0083_mpesapayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='MpesaRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=100)),
                ('merchant', models.CharField(max_length=50, unique=True)),
                ('status', models.CharField(default='PENDING', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='MpesaTransaction',
        ),
    ]
