# Generated by Django 5.0.6 on 2024-06-12 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_teacher_team_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='team',
            new_name='date_of',
        ),
    ]
