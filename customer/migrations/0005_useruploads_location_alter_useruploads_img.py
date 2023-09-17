# Generated by Django 4.2.4 on 2023-09-09 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_remove_useruploads_profilepic_profilepictures'),
    ]

    operations = [
        migrations.AddField(
            model_name='useruploads',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='useruploads',
            name='img',
            field=models.ImageField(upload_to='user_uploads', verbose_name='Upload Images'),
        ),
    ]
