# Generated by Django 4.2.4 on 2023-09-09 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_remove_useruploads_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelinvites',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='useruploads',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
