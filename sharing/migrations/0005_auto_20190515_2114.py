# Generated by Django 2.1.3 on 2019-05-15 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharing', '0004_profile_payment_plan_activation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='payment_plan_activation_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
