# Generated by Django 5.0.6 on 2024-06-27 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_author_writed_books_alter_genre_authors_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=1, verbose_name='Текст комментария'),
            preserve_default=False,
        ),
    ]
