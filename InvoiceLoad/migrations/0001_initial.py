# Generated by Django 2.2.4 on 2019-08-18 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('actif', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Bankaccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('actif', models.BooleanField(default=True)),
                ('iban', models.CharField(blank=True, max_length=200)),
                ('bban', models.CharField(blank=True, max_length=200)),
                ('swift', models.CharField(blank=True, max_length=200)),
                ('is_default', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('actif', models.BooleanField(default=True)),
                ('mail', models.EmailField(blank=True, max_length=254)),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Costcenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('actif', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('nb_decimal', models.IntegerField(default=2)),
                ('actif', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Paymentmethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('actif', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('actif', models.BooleanField(default=True)),
                ('taux', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('actif', models.BooleanField(default=True)),
                ('auto_replace', models.BooleanField(default=True)),
                ('move_day_1', models.IntegerField()),
                ('eom_1', models.BooleanField(default=True)),
                ('move_day_2', models.IntegerField()),
                ('eom_2', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('actif', models.BooleanField(default=True)),
                ('mail', models.EmailField(blank=True, max_length=254)),
                ('num_tva', models.CharField(blank=True, max_length=200)),
                ('iban', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='InvoiceLoad.Bankaccount', verbose_name='Iban du fournisseur')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('date', models.DateField()),
                ('inv_number', models.CharField(max_length=200)),
                ('po_number', models.CharField(blank=True, max_length=200)),
                ('net', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Montant HT facture')),
                ('gross', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Montant TTC facture')),
                ('tax', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Montant TVA facture')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='InvoiceLoad.Currency', verbose_name='Devise de la facture')),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
        migrations.CreateModel(
            name='Imputation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('number', models.CharField(max_length=200)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InvoiceLoad.Invoice', verbose_name='Imputation facture')),
            ],
        ),
        migrations.CreateModel(
            name='Exchangerate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, unique=True)),
                ('date_valid_from', models.DateField()),
                ('rate', models.DecimalField(decimal_places=10, max_digits=20, verbose_name='Taux de change')),
                ('currency_from', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Currency_one', to='InvoiceLoad.Currency', verbose_name='Devise initiale')),
                ('currency_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Currency_two', to='InvoiceLoad.Currency', verbose_name='Devise cible')),
            ],
            options={
                'ordering': ['code'],
            },
        ),
    ]
