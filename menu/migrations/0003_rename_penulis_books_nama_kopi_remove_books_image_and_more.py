# Generated by Django 5.0 on 2024-01-02 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_books_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='penulis',
            new_name='nama_kopi',
        ),
        migrations.RemoveField(
            model_name='books',
            name='image',
        ),
        migrations.RemoveField(
            model_name='books',
            name='judul',
        ),
        migrations.RemoveField(
            model_name='books',
            name='tanggal_terbit',
        ),
    ]