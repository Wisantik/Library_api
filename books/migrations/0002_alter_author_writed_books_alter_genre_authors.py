# Generated by Django 5.0.6 on 2024-06-27 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='writed_books',
            field=models.ManyToManyField(blank=True, to='books.book', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='genre',
            name='authors',
            field=models.ManyToManyField(to='books.author', verbose_name='Авторы которые пишут в этом жанре'),
        ),
    ]
