# Generated by Django 2.1.3 on 2019-05-14 19:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sharing', '0003_auto_20190513_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='payment_plan_activation_time',
            field=models.TimeField(auto_now_add=True,
                                   default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
