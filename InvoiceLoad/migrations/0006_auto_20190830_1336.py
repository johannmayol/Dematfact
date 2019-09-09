# Generated by Django 2.2.4 on 2019-08-30 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InvoiceLoad', '0005_auto_20190829_1047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'ordering': ['code'], 'verbose_name': 'Currency', 'verbose_name_plural': 'Currencies'},
        ),
        migrations.AddField(
            model_name='invoice',
            name='supplier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='InvoiceLoad.Supplier', verbose_name='Fournisseur de la facture'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='image',
            field=models.FileField(upload_to='invoice/image/'),
        ),
    ]
