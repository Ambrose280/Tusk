# Generated by Django 4.2.4 on 2023-09-11 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tuskcourses", "0021_alter_course_course_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="course_image",
            field=models.ImageField(
                blank=True,
                default="courseimgs/70-702065_django-python-logo-apress-the-definitive-guide-to_T18MEpY.png",
                null=True,
                upload_to="courseimgs",
                verbose_name="Course Image",
            ),
        ),
    ]
