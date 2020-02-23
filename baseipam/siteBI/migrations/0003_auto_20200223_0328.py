# Generated by Django 2.2.8 on 2020-02-23 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteBI', '0002_auto_20191120_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(default='Por definir', max_length=30, verbose_name='Nome: ')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Logo: ')),
            ],
            options={
                'verbose_name': 'Imagem SlideShow',
                'verbose_name_plural': 'Imagens SlideShow',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Por definir', max_length=30, verbose_name='Nome: ')),
                ('tag', models.CharField(choices=[('outros', 'Outros'), ('estudos', 'Mercado'), ('comunicacao', 'Comunicação'), ('marketing', 'Marketing'), ('comercial', 'Comercial'), ('estudos comercial', 'Mercado e Comercial'), ('estudos comunicacao', 'Mercado e Comunicação'), ('comunicacao marketing', 'Comunicação e Marketing')], default='outros', max_length=100)),
                ('image', models.ImageField(upload_to='images/', verbose_name='Logo: ')),
            ],
            options={
                'verbose_name': 'Imagem Portfolio',
                'verbose_name_plural': 'Imagens Portofolio',
            },
        ),
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name': 'Texto', 'verbose_name_plural': 'Textos'},
        ),
    ]
