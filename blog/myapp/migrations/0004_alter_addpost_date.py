# Generated by Django 4.1.1 on 2022-09-12 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_alter_addpost_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="addpost",
            name="date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
