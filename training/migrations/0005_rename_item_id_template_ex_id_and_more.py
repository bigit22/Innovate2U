# Generated by Django 4.2.4 on 2023-12-08 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='template',
            old_name='item_id',
            new_name='ex_id',
        ),
        migrations.RemoveField(
            model_name='template',
            name='type_id',
        ),
    ]
