# Generated by Django 3.2.18 on 2023-06-07 08:11

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20230607_0811'),
        ('cryptocoins', '0003_auto_20230302_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='BNBWithdrawalApprove',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.withdrawalrequest',),
        ),
        migrations.CreateModel(
            name='BTCWithdrawalApprove',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.withdrawalrequest',),
        ),
        migrations.CreateModel(
            name='ETHWithdrawalApprove',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.withdrawalrequest',),
        ),
        migrations.CreateModel(
            name='TRXWithdrawalApprove',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.withdrawalrequest',),
        ),
        migrations.AlterField(
            model_name='depositswithdrawalsstats',
            name='stats',
            field=models.JSONField(default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
        migrations.AlterField(
            model_name='gaskeeper',
            name='extra',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='keeper',
            name='extra',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='transactioninputscore',
            name='data',
            field=models.JSONField(default=dict),
        ),
    ]