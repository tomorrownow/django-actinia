# Generated by Django 4.2.7 on 2024-03-18 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("grass", "0006_location_slug_mapset_slug"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="location",
            options={"ordering": ["-updated_on"]},
        ),
    ]
