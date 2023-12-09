# Generated by Django 4.2.7 on 2023-12-09 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0003_alter_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='discussions.tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
