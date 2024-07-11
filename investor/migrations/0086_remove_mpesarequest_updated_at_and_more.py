# Generated by Django 4.2.9 on 2024-07-11 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('investor', '0085_alter_mpesarequest_merchant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mpesarequest',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='mpesarequest',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mpesarequest',
            name='merchant',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mpesarequest',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='mpesarequest',
            name='status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='mpesarequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
