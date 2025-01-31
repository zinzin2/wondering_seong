# Generated by Django 2.0.13 on 2019-07-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(0, 'basic'), (1, 'emergency'), (2, 'news')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='kinds',
            field=models.PositiveSmallIntegerField(choices=[(0, 'card'), (1, 'post')]),
        ),
    ]
