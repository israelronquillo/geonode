# Generated by Django 2.2.10 on 2020-03-04 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0030_auto_20200221_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupprofile',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='groupprofile',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
        ),
    ]
