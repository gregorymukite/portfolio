# Generated by Django 5.1 on 2024-08-29 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_slideimage_delete_dashboard_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideimage',
            name='text',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
