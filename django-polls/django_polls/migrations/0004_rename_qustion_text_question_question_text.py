# Generated by Django 5.0.2 on 2024-02-12 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_questions_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='qustion_text',
            new_name='question_text',
        ),
    ]
