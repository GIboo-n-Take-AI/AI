# Generated by Django 4.2.4 on 2023-08-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0003_alter_notice_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='notice_image',
            field=models.ImageField(null=True, upload_to='notice/type/%Y/%m/%d'),
        ),
    ]