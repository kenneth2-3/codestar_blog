# Generated by Django 4.2.23 on 2025-07-04 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_on']},
        ),
    ]
