# Generated by Django 5.1 on 2024-08-29 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_dashboard_profile_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='about_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_img1', models.ImageField(upload_to='about_images')),
                ('a_img2', models.ImageField(upload_to='about_images')),
            ],
        ),
    ]
