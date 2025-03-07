# Generated by Django 5.1.6 on 2025-02-25 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecategory',
            options={'ordering': ['name'], 'verbose_name': 'Article Category', 'verbose_name_plural': 'Article Categories'},
        ),
        migrations.RemoveField(
            model_name='articlecategory',
            name='desc',
        ),
        migrations.AddField(
            model_name='articlecategory',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
