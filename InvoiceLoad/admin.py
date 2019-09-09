from django.contrib import admin
from .models import *

admin.site.site_header = (u"Administration de DematFact")
admin.site.index_title = (u"DematFact")


# from import_export import resources
# from core.models import Book

# class BookResource(resources.ModelResource):

#     class Meta:
#         model = Book



# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')
    list_filter = ('actif',)

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')
    list_filter = ('actif',)
    filter_horizontal = ('ibans',)

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'number')

class BankaccountAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')
    list_filter = ('actif',)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')
    list_filter = ('actif',)

class CostcenterAdmin (admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')
    list_filter = ('actif',)

class TaxAdmin (admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')
    list_filter = ('actif',)

class TermAdmin (admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')
    list_filter = ('actif',)

class CurrencyAdmin (admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')
    list_filter = ('actif',)

class PaymentmethodAdmin (admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')
    list_filter = ('actif',)

class ExchangerateAdmin (admin.ModelAdmin):
    list_display = ('currency_from','currency_to','rate','date_valid_from',)
    search_fields = ('currency_from',)
    list_filter = ('currency_from','currency_to','date_valid_from',)

admin.site.register(Company, CompanyAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Bankaccount, BankaccountAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Costcenter, CostcenterAdmin)
admin.site.register(Tax, TaxAdmin)
admin.site.register(Term, TermAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Exchangerate, ExchangerateAdmin)