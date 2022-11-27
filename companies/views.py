from django.shortcuts import render, redirect, get_object_or_404
from .models import CompanyModel

from .forms import AddCompanyForm

# Create your views here.
def company_list(request):
    companies = CompanyModel.objects.all()
    return render (request, 'companies/company_list.html',{'companies':companies})

def company_details(request, pk):
    companies = get_object_or_404(CompanyModel, pk=pk)
    return render (request, 'companies/company_detials.html',{'companies':companies})


def company_delete(request, pk):
    companies = CompanyModel.objects.get(pk=pk)
    companies.delete()
    return redirect('company_list')


def add_company(request):
    if request.method == 'POST':
        company_form = AddCompanyForm(request.POST)
        if company_form.is_valid():
            company_form.save()
            return redirect('company_list')
    
    else:
        company_form = AddCompanyForm()
    return render(request, 'companies/company-add_edit.html',{'company_form':company_form})


def edit_company(request, pk):
    companies = get_object_or_404(CompanyModel, pk=pk)
    if request.method == 'POST':
        company_form = AddCompanyForm(request.POST, instance=companies)
        if company_form.is_valid():
            company_form.save()
            return redirect('company_list')
    
    else:
        company_form = AddCompanyForm(instance=companies)
    return render(request, 'companies/company-add_edit.html',{'company_form':company_form})


