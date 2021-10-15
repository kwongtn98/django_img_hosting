# Generated by Django 3.2.8 on 2021-10-15 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('thumbnail_path', models.TextField()),
                ('ori_path', models.TextField()),
                ('img_str', models.TextField()),
                ('keywords', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keywords', to='img.keyword')),
            ],
        ),
    ]
