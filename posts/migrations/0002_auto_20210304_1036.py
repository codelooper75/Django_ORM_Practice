# Generated by Django 3.1.7 on 2021-03-04 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.editor'),
        ),
    ]
