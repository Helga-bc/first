# Generated by Django 4.1.7 on 2023-07-02 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0019_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='raiting',
            field=models.IntegerField(),
        ),
    ]
