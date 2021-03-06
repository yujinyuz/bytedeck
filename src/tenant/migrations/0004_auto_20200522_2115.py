# Generated by Django 2.2.12 on 2020-05-23 04:15

from django.db import migrations, models
import tenant.models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0003_auto_20200405_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='name',
            field=models.CharField(help_text='The name may only include lowercase letters, numbers, and dashes.         It must start with a letter, and may not end in a dash, nor include consecutive dashes', max_length=62, unique=True, validators=[tenant.models.check_tenant_name]),
        ),
    ]
