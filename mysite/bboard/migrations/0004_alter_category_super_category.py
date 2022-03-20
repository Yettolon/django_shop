# Generated by Django 3.2 on 2022-03-12 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_auto_20220312_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='super_category',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, to='bboard.supercategory', verbose_name='Main Category'),
        ),
    ]
