# Generated by Django 2.2.1 on 2019-05-23 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_auto_20190524_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
