# Generated by Django 5.0.1 on 2024-03-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0002_alter_jobs_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='exp',
            field=models.IntegerField(),
        ),
    ]
