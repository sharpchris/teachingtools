# Generated by Django 3.0.6 on 2020-05-28 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filtertools', '0003_auto_20200527_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='tooltip',
            field=models.CharField(default='Tooltip', max_length=255),
            preserve_default=False,
        ),
    ]
