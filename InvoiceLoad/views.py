from django.shortcuts import render
from InvoiceLoad.models import Invoice, Imputation
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.detail import DetailView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from django.utils import timezone


# Create your views here.

@login_required
def invoice_home(request):
    """View function for home page of site."""
    # Generate counts
    nb_invoice = Invoice.objects.all().count()
    nb_invoice_received = Invoice.objects.filter(status__exact='received').count()
# Note: You can use underscores (__) to navigate as many levels of relationships (ForeignKey/ManyToManyField) as you like. For example, a Book that had different types, defined using a further "cover" relationship might have a parameter name: type__cover__name__exact='hard'.
    context = {
        'nb_invoice': nb_invoice,
        'nb_invoice_received': nb_invoice_received,
    }
    return render(request, 'InvoiceLoad/invoice_home.html', context=context)

# Invoice
class InvoiceListView(ListView):
    model = Invoice
    context_object_name = 'Facture'
    queryset_list = Invoice.objects.all

class InvoiceDetailView(DetailView):
    model = Invoice
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context_object_name = 'Détail facture'
        return context

class InvoiceCreate(LoginRequiredMixin, CreateView):
    model = Invoice
    fields = '__all__'
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class InvoiceUpdate(UpdateView):
    model = Invoice
    fields = '__all__' #['first_name', 'last_name', 'date_of_birth', 'date_of_death']

class InvoiceDelete(DeleteView):
    model = Invoice
    success_url = reverse_lazy('invoice_home')


def imputation_create(request, Invoice_id):
    invoice = invoice.objects.get(pk=invoice_id)
    ImputationInlineFormSet = inlineformset_factory(Invoice, Imputation, fields='__all__')
    if request.method == "POST":
        formset = ImputationInlineFormSet(request.POST, request.FILES, instance=invoice)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(invoice.get_absolute_url())
    else:
        formset = ImputationInlineFormSet(instance=invoice)
    return render(request, 'invoice_form.html', {'formset': formset})