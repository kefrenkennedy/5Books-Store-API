# Generated by Django 4.1.2 on 2022-11-07 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
        ("books", "0003_alter_book_amount_alter_book_diameter_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="books",
                to="categories.categories",
            ),
        ),
    ]