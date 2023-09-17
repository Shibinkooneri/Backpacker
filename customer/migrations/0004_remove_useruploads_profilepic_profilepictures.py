# Generated by Django 4.2.4 on 2023-09-09 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0003_useruploads_profilepic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useruploads',
            name='profilepic',
        ),
        migrations.CreateModel(
            name='Profilepictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='profile_pics', verbose_name='profile pics')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]