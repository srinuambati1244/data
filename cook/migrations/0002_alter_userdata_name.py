# Generated by Django 3.2 on 2021-05-20 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]