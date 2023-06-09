# Generated by Django 4.1.7 on 2023-04-13 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appMy', '0005_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='İsim')),
                ('image', models.ImageField(upload_to=None, verbose_name='Dizi-Film')),
                ('slug', models.SlugField(blank=True, verbose_name='Slug')),
            ],
        ),
    ]
