# Generated by Django 2.1.7 on 2019-03-04 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20190304_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='saved_scores',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
