# Generated by Django 4.2.7 on 2023-11-13 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_about_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('position', models.CharField(max_length=60, verbose_name='Position')),
                ('text', models.TextField(verbose_name='Text')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
            ],
        ),
    ]