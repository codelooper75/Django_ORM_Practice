# Generated by Django 3.1.7 on 2021-03-04 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr_mosh', '0002_auto_20210304_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='reporst_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hr_mosh.employees'),
        ),
    ]
