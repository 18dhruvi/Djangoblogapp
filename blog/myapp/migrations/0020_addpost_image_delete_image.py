# Generated by Django 4.1.1 on 2022-09-28 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0019_rename_title_image_addpost"),
    ]

    operations = [
        migrations.AddField(
            model_name="addpost",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.DeleteModel(
            name="Image",
        ),
    ]
