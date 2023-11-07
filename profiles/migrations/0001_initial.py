# Generated by Django 4.2.7 on 2023-11-07 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20, null=True)),
                ('birth_day', models.DateField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('bio', models.CharField(max_length=200, null=True)),
                ('is_moderator', models.BooleanField(default=False)),
                ('last_access', models.DateField(auto_now=True)),
                ('avatar_img', models.ImageField(blank=True, null=True, upload_to=profiles.models.upload_avatar_img)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
