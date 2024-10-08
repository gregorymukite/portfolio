# Generated by Django 5.1 on 2024-09-18 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0011_skill_cartegory_remove_skills_user_skill_set_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workexperience',
            name='user',
        ),
        migrations.AddField(
            model_name='about',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='PersonalDetails',
        ),
    ]
