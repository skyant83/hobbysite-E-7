# Generated by Django 5.1.6 on 2025-03-07 04:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_article_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.articlecategory', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Dated Created'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Article Title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Last Updated'),
        ),
    ]
