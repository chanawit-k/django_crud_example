from typing import Any
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Employee

class EmployeeListView(ListView):
    model = Employee
    template_name = 'payroll/employeelist.html'
    context_object_name = 'employee_list'
    paginate_by = 10

    def get_queryset(self):
        # select_related('EmpDepartment'), Django prefetches the related 
        return Employee.objects.select_related('EmpDepartment', 'EmpCountry').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'payroll/employee_detail.html'
    queryset = Employee.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
