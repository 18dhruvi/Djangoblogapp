# Generated by Django 4.1.1 on 2022-09-28 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0020_addpost_image_delete_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="addpost",
            name="image",
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
                (
                    "addpost",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.addpost",
                    ),
                ),
            ],
        ),
    ]
