# Generated by Django 4.0.3 on 2022-04-14 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_rename_utilisateur_review_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='title',
            new_name='titre',
        ),
    ]
