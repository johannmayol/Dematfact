from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from InvoiceLoad.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.invoice_home, name='invoice_home'),
    path('list/', InvoiceListView.as_view(), name='invoice_list'),
    path('create/', views.InvoiceCreate.as_view(), name='invoice_create'),
    path('détail/<int:pk>/', InvoiceDetailView.as_view(), name='invoice_detail'),
    path('<int:pk>/update/', views.InvoiceUpdate.as_view(), name='invoice_update'),
    path('<int:pk>/delete/', views.InvoiceDelete.as_view(), name='invoice_delete'),
    path('<int:pk>/imputations/create/', views.imputation_create, name='imputation_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)