# Generated by Django 3.1.5 on 2021-04-27 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210409_1705'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['code']},
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=10),
        ),
    ]
