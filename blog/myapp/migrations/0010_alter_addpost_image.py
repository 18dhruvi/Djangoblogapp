# Generated by Django 4.1.1 on 2022-09-23 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0009_addpost_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="addpost",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]