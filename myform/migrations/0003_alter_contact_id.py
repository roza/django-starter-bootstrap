# Generated by Django 4.1.2 on 2022-10-05 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myform', '0002_auto_20180925_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]