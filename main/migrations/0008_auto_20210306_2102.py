# Generated by Django 3.1.4 on 2021-03-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210306_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='exam_number',
            field=models.IntegerField(default=0),
        ),
    ]
