# Generated by Django 3.0.6 on 2020-05-09 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mobile_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
