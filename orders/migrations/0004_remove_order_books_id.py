# Generated by Django 4.1.2 on 2022-11-07 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0003_order_books_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="books_id",
        ),
    ]
