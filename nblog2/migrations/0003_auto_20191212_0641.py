# Generated by Django 3.0 on 2019-12-11 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nblog2', '0002_note_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='タイトル'),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=100, verbose_name='タイトル'),
        ),
    ]
