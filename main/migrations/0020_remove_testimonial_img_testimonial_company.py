# Generated by Django 5.0.1 on 2024-02-25 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_info_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='img',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='Company',
            field=models.CharField(max_length=50, null=True, verbose_name='Company Name'),
        ),
    ]