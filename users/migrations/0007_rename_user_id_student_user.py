# Generated by Django 5.0.4 on 2024-06-02 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_student_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='user_id',
            new_name='user',
        ),
    ]