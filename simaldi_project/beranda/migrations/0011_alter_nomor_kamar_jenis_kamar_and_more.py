# Generated by Django 4.2.1 on 2023-06-19 01:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beranda', '0010_rename_status_konfirmasi_pembayaran_status_konfirmasi_pembayaran'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomor_kamar',
            name='jenis_kamar',
            field=models.CharField(choices=[('VVIP', 'VVIP'), ('Executive Class', 'Executive Class'), ('Superior Room', 'Superior Room'), ('Deluxe Room', 'Deluxe Room'), ('Family Room', 'Family Room'), ('Single Room', 'Single Room')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pemesanan',
            name='tanggal_checkin',
            field=models.DateField(default=datetime.date(2023, 6, 19)),
        ),
    ]
