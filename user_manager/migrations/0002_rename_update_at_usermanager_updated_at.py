# Generated by Django 4.1 on 2022-09-06 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_manager", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usermanager",
            old_name="update_at",
            new_name="updated_at",
        ),
    ]
