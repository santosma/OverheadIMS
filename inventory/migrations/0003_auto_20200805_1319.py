# Generated by Django 3.0.8 on 2020-08-05 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20200805_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemlocation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
