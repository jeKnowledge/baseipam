# Generated by Django 2.2.7 on 2019-11-20 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteBI', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='english_content',
            new_name='eng_content',
        ),
        migrations.RenameField(
            model_name='content',
            old_name='portuguese_content',
            new_name='pt_content',
        ),
    ]
