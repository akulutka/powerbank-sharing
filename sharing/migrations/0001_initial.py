# Generated by Django 2.1.3 on 2019-04-26 16:45

from django.conf import settings
from django.db import migrations, models
from django.db.models.deletion import SET_NULL, SET_DEFAULT, CASCADE


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('order_type', models.CharField(default='hold',
                                                max_length=128)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('progress', models.CharField(default='created',
                                              max_length=128)),
                ('reservation_time', models.IntegerField(default=15)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentPlan',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('name', models.CharField(default='Обычный', max_length=128)),
                ('description', models.CharField(default='Самый ' +
                                                 'обычный тариф.',
                                                 max_length=512)),
                ('payment_type', models.CharField(default='perminute',
                                                  max_length=128)),
                ('cost', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Powerbank',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('capacity', models.IntegerField()),
                ('location', models.IntegerField()),
                ('status', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('name', models.CharField(max_length=512, null=True)),
                ('active_mail', models.BooleanField(default=False)),
                ('photo', models.FileField(upload_to='users/')),
                ('passport', models.FileField(upload_to='passports/')),
                ('passport_status', models.CharField(default='empty',
                                                     max_length=216)),
                ('wallets', models.CharField(default='', max_length=512)),
                ('payment_plans', models.CharField(default='',
                                                   max_length=512)),
                ('hold',
                    models.ForeignKey(null=True,
                                      on_delete=SET_NULL,
                                      to='sharing.Powerbank')),
                ('user',
                    models.ForeignKey(on_delete=CASCADE,
                                      to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=512)),
                ('crds_lot', models.FloatField()),
                ('crds_lat', models.FloatField()),
                ('time', models.TimeField(auto_now_add=True)),
                ('qrcode', models.CharField(default='Hello, world!',
                                            max_length=512)),
                ('ip', models.CharField(default='127.0.0.1',
                                        max_length=256)),
                ('free_pbs', models.IntegerField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('name', models.CharField(default='Кошелёк', max_length=128)),
                ('balance', models.FloatField(default=0.0)),
                ('status', models.CharField(default='active', max_length=128)),
                ('payment_method', models.CharField(default='promo',
                                                    max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment_plan',
            field=models.ForeignKey(null=True,
                                    on_delete=SET_NULL,
                                    to='sharing.PaymentPlan'),
        ),
        migrations.AddField(
            model_name='order',
            name='pb',
            field=models.ForeignKey(null=True,
                                    on_delete=SET_NULL,
                                    to='sharing.Powerbank'),
        ),
        migrations.AddField(
            model_name='order',
            name='profile',
            field=models.ForeignKey(null=True,
                                    on_delete=SET_NULL,
                                    to='sharing.Profile'),
        ),
        migrations.AddField(
            model_name='order',
            name='share',
            field=models.ForeignKey(null=True,
                                    on_delete=SET_NULL,
                                    to='sharing.Share'),
        ),
        migrations.AddField(
            model_name='order',
            name='wallet',
            field=models.ForeignKey(null=True,
                                    on_delete=SET_NULL,
                                    to='sharing.Wallet'),
        ),
    ]
