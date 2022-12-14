# Generated by Django 4.1.1 on 2022-09-26 10:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0015_alter_addpost_date_alter_comment_created_on"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="addpost",
            options={"verbose_name": "Addpost"},
        ),
        migrations.RemoveField(
            model_name="contact",
            name="subject",
        ),
        migrations.AddField(
            model_name="contact",
            name="date",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="contact",
            name="title",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="myapp.addpost",
            ),
        ),
    ]
