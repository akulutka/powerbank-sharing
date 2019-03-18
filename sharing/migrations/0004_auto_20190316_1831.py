# Generated by Django 2.1.3 on 2019-03-16 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharing', '0003_auto_20190310_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Powerbank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('value', models.IntegerField()),
                ('location', models.CharField(max_length=512)),
                ('status', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='share',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
