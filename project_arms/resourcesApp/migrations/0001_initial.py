# Generated by Django 4.2.6 on 2023-12-16 10:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Resources",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=250)),
                ("last_name", models.CharField(max_length=250)),
                ("email", models.EmailField(max_length=250)),
                ("phone", models.BigIntegerField()),
                ("graduation", models.CharField(max_length=500)),
                ("stream", models.CharField(max_length=100)),
                ("year", models.SmallIntegerField()),
                ("pg", models.CharField(max_length=500, null=True)),
                ("pg_stream", models.CharField(max_length=100, null=True)),
                ("pg_year", models.SmallIntegerField(null=True)),
                ("trained_technology", models.CharField(max_length=250)),
                ("institute_name", models.CharField(max_length=500)),
                ("duration_course", models.CharField(max_length=100)),
                ("reference_name", models.CharField(max_length=250, null=True)),
                ("hear_interview", models.CharField(max_length=100, null=True)),
                ("work_experience", models.CharField(max_length=100, null=True)),
                ("years_experience", models.SmallIntegerField(null=True)),
                ("company_name", models.CharField(max_length=500, null=True)),
                ("current_ctc", models.FloatField(null=True)),
                ("expected_ctc", models.FloatField(null=True)),
                ("pf", models.CharField(max_length=100, null=True)),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime(2023, 12, 16, 15, 37, 22, 626814)
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Rounds",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("online_marks", models.FloatField()),
                ("is_online_passed", models.BooleanField(default=False)),
                ("online_feedback", models.TextField()),
                ("communication_marks", models.FloatField()),
                ("is_communication_passed", models.BooleanField(default=False)),
                ("communication_feedback", models.TextField()),
                ("technical_marks", models.FloatField()),
                ("is_technical_passed", models.BooleanField(default=False)),
                ("technical_feedback", models.TextField()),
                ("is_qualified", models.BooleanField(default=False)),
                ("is_ceo_passed", models.BooleanField(default=False)),
                (
                    "resource_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="resourcesApp.resources",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OnBoarded",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("onboard_status", models.BooleanField(default=False)),
                (
                    "rounds_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="resourcesApp.rounds",
                    ),
                ),
            ],
        ),
    ]
