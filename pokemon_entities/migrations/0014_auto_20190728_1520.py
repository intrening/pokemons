# Generated by Django 2.2.3 on 2019-07-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0013_auto_20190728_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='название на английском'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='название на японском'),
            preserve_default=False,
        ),
    ]
