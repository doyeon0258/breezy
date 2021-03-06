# Generated by Django 3.1.5 on 2021-05-07 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210430_1420'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['code'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='post/no_image.png', upload_to='post/%Y/%m/%d'),
        ),
    ]
