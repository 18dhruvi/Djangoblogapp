# Generated by Django 4.1.1 on 2022-09-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0023_remove_addpost_image_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.ImageField(default="", upload_to="images/"),
            preserve_default=False,
        ),
    ]
