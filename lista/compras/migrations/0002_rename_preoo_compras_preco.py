# Generated by Django 4.1.7 on 2023-04-12 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compras',
            old_name='preoo',
            new_name='preco',
        ),
    ]