# Generated by Django 3.1.8 on 2023-04-18 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={},
        ),
        migrations.RenameField(
            model_name='client',
            old_name='project_name',
            new_name='client_name',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='project_name',
        ),
    ]
