# Generated by Django 5.1.3 on 2024-11-27 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0002_repository_time_limit"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="role",
            field=models.CharField(
                choices=[("lead", "Tech-lead"), ("contributor", "Contributor")],
                default="contributor",
                max_length=11,
            ),
        ),
    ]
