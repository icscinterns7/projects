# Generated by Django 4.1.3 on 2022-11-20 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_address_author_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='book_outlet.address'),
        ),
    ]