# Generated by Django 4.0.3 on 2022-04-14 17:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_rename_title_review_titre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='time_created',
            new_name='date_creation',
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(blank=True, max_length=8192, verbose_name='Commentaire'),
        ),
        migrations.AlterField(
            model_name='review',
            name='note',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='note'),
        ),
        migrations.AlterField(
            model_name='review',
            name='titre',
            field=models.CharField(max_length=128, verbose_name='Titre de la critique'),
        ),
    ]