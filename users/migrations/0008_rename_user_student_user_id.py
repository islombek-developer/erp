# Generated by Django 5.0.4 on 2024-06-02 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_user_id_student_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='user',
            new_name='user_id',
        ),
    ]
