# Generated by Django 2.2 on 2019-05-01 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_auto_20190501_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='cover',
            field=models.ImageField(default='cover1.img', upload_to='services/'),
            preserve_default=False,
        ),
    ]
