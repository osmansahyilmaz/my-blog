# Generated by Django 4.1 on 2024-02-01 21:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 2, 1, 21, 29, 24, 508320, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 2, 1, 21, 29, 24, 508320, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
