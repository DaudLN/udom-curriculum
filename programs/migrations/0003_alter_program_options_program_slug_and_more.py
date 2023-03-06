# Generated by Django 4.1.4 on 2023-03-06 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programs", "0002_alter_program_college_alter_program_competences_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="program",
            options={"ordering": ["name"]},
        ),
        migrations.AddField(
            model_name="program",
            name="slug",
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="program",
            name="college",
            field=models.CharField(
                choices=[
                    ("COLLEGE OF EDUCATION (CoED)", "COLLEGE OF EDUCATION (CoED)"),
                    (
                        "COLLEGE OF INFORMATICS AND VIRTUAL EDUCATION (CIVE)",
                        "COLLEGE OF INFORMATICS AND VIRTUAL EDUCATION (CIVE)",
                    ),
                    (
                        "COLLEGE OF HEALTH AND ALLIED SCIENCES (CHAS)",
                        "COLLEGE OF HEALTH AND ALLIED SCIENCES (CHAS)",
                    ),
                    (
                        "COLLEGE OF HUMANITIES AND SOCIAL SCIENCES (CHSS)",
                        "COLLEGE OF HUMANITIES AND SOCIAL SCIENCES (CHSS)",
                    ),
                    (
                        "COLLEGE OF EARTH SCIENCES (CoES)",
                        "COLLEGE OF EARTH SCIENCES (CoES)",
                    ),
                ],
                default="COLLEGE OF HEALTH AND ALLIED SCIENCES (CHAS)",
                max_length=255,
            ),
        ),
    ]
