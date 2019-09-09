from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

# Nécessaire pour maintenir __str__ à la place de __unicode__ dans les définitions de noms si regression en python 2 
# @python_2_str_compatible 
# from __future__ import str_literals
# from django.utils.encoding import python_2_str_compatible

# Create your models here.

class Company(models.Model):
    actif = models.BooleanField(default = True)
    code = models.CharField(max_length=200, unique = True)
    name = models.CharField(max_length=200)
    mail = models.EmailField(max_length=254, blank = True)
    class Meta:
        ordering = ['code']

    def __str__(self):
        return u"{0} - {1}".format(self.name, self.code)



class Supplier(models.Model):
    actif = models.BooleanField(default = True)
    code = models.CharField(max_length=200, unique = True)
    name = models.CharField(max_length=200)
    mail = models.EmailField(max_length=254, blank = True)
    num_tva = models.CharField(max_length=200, blank = True) 
    ibans = models.ManyToManyField('Bankaccount', blank=True, verbose_name = 'Ibans du fournisseur')
    class Meta:
        ordering = ['name']

    def __str__(self):
        return u"{0} - {1}".format(self.name, self.code)

class Bankaccount(models.Model):
    actif = models.BooleanField(default = True)
    code = models.CharField(max_length=200, unique = True)
    name = models.CharField(max_length=200, blank = True)
    iban = models.CharField(max_length=200, blank = True)
    bban = models.CharField(max_length=200, blank = True)
    swift = models.CharField(max_length=200, blank = True)
    is_default = models.BooleanField()
    def __str__(self):
        return u"{0}".format(self.code)

class Invoice(models.Model):
    INVOICE_STATUS = (
        ('1', 'Reçue'),
        ('2', 'En cours de validation'),
        ('3', 'Renvoyée'),
        ('4', 'Approuvée'),
        ('5', 'Transmise'),
        ('90', 'Payée'),
        ('99', 'Supprimée'),
    )
    status = models.CharField(max_length=2, choices=INVOICE_STATUS, default='1')
    created_date = models.DateTimeField(default=timezone.now)
    date = models.DateField()
    supplier = models.ForeignKey('Supplier', on_delete = models.PROTECT, verbose_name ='Fournisseur de la facture')
    inv_number = models.CharField(max_length=200)
    po_number = models.CharField(max_length=200, blank = True)
    currency = models.ForeignKey('Currency', on_delete = models.PROTECT, verbose_name ='Devise de la facture')
    net   = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Montant HT facture")
    gross  = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Montant TTC facture")
    tax  = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Montant TVA facture")
    image = models.FileField(upload_to='invoice/image/')
    class Meta:
        ordering = ['created_date']
    # def get_absolute_url(self):
    #     """Returns the url to access a detail record for this invoice."""
    #     return reverse('invoice-detail', args=[str(self.id)])
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('invoice_detail', args=[str(self.id)])


class Imputation(models.Model):
	# number = models.AutoField()
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE, verbose_name='Imputation facture')
    created_date = models.DateTimeField(default=timezone.now)
    number = models.CharField(max_length=200)
    def __str__(self):
    	return u"{0} - {1}".format(self.invoice.inv_number, self.number)

class Account(models.Model):
    actif = models.BooleanField(default = True)
    code = models.CharField(max_length=200, unique = True)
    name = models.CharField(max_length=200)
    class Meta:
        ordering = ['code']
    def __str__(self):
        return u"{0} - {1}".format(self.name, self.code)

class Costcenter(models.Model):
    actif = models.BooleanField(default = True)
    code = models.CharField(max_length=200, unique = True)
    name = models.CharField(max_length=200)
    class Meta:
        ordering = ['code']
    def __str__(self):
        return u"{0} - {1}".format(self.name, self.code)

class Tax(models.Model):
    actif = models.BooleanField(default = True)
    code = models.CharField(max_length=200, unique = True)
    name = models.CharField(max_length=200)
    taux = models.CharField(max_length=200)
    class Meta:
        ordering = ['code']
    def __str__(self):
        return u"{0} - {1}".format(self.name, self.code)

class Term(models.Model):
    actif = models.BooleanField(default = True)
    code = models.CharField(max_length=200, unique = True)
    name = models.CharField(max_length=200)
    auto_replace = models.BooleanField(default = True)
    move_day_1 = models.IntegerField()
    eom_1 = models.IntegerField()
    move_day_2 = models.IntegerField()
    eom_2 = models.IntegerField()
    class Meta:
        ordering = ['code']
    def __str__(self):
        return u"{0} - {1}".format(self.name, self.code)

class Currency(models.Model):
    actif = models.BooleanField(default = True)
    code = models.CharField(max_length=200, unique = True)
    name = models.CharField(max_length=200)
    nb_decimal = models.IntegerField(default = 2)
    class Meta:
        ordering = ['code']
        verbose_name = _(u"Currency")
        verbose_name_plural = _(u"Currencies")
    def __str__(self):
        return u"{0} - {1}".format(self.name, self.code)

class Paymentmethod(models.Model):
    actif = models.BooleanField(default = True)
    code = models.CharField(max_length=200, unique = True)
    name = models.CharField(max_length=200)
    class Meta:
        ordering = ['code']
    def __str__(self):
        return u"{0} - {1}".format(self.name, self.code)

class Exchangerate(models.Model):
    currency_from = models.ForeignKey('Currency', on_delete = models.PROTECT, verbose_name ='Devise initiale', related_name = 'Currency_one')
    currency_to = models.ForeignKey('Currency', on_delete = models.PROTECT, verbose_name ='Devise cible', related_name = 'Currency_two')
    date_valid_from = models.DateField()
    rate  = models.DecimalField(max_digits=20, decimal_places=10, verbose_name="Taux de change")
    class Meta:
        ordering = ['currency_from', 'date_valid_from',]
        unique_together = ['currency_from', 'currency_to', 'date_valid_from']
    def __str__(self):
        return u"{0}".format(self.code)
