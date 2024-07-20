# Generated by Django 5.0.4 on 2024-07-11 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0002_image_thumbnail"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="main",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="image",
            name="thumbnail",
            field=models.ImageField(blank=True, upload_to="product_images/thumbnails"),
        ),
    ]
