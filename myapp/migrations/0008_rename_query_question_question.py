# Generated by Django 5.0.6 on 2024-12-11 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_question_delete_member_delete_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='query',
            new_name='question',
        ),
    ]