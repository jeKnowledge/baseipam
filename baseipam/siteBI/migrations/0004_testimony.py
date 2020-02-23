# Generated by Django 2.2.8 on 2020-02-23 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteBI', '0003_auto_20200223_0328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=300, verbose_name='Link: ')),
                ('subtitle', models.CharField(max_length=30, verbose_name='Subtítulo: ')),
            ],
            options={
                'verbose_name': 'Link para os testemunhos',
                'verbose_name_plural': 'Links para os testemunhos',
            },
        ),
    ]