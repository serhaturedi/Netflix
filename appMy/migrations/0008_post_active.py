# Generated by Django 4.1.7 on 2023-04-13 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0007_post_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='active',
            field=models.BooleanField(null=True, verbose_name='Aktif'),
        ),
    ]
