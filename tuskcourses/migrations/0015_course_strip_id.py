# Generated by Django 4.2.4 on 2023-09-08 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "tuskcourses",
            "0014_remove_courseusers_courses_remove_courseusers_user_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="strip_id",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
