# Generated by Django 4.2.1 on 2023-06-05 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('width', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('parent_picture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='api.picture')),
            ],
        ),
    ]
