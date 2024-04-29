
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
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
    
class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('payroll:employee_list')

    def get_queryset(self):
        return super().get_queryset().select_related('EmpDepartment', 'EmpCountry')
    
class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = [ 
        "FirstName", 
        "LastName"
    ] 
    success_url = reverse_lazy('payroll:employee_list')

class EmployeeCreateView(CreateView):
    model = Employee
    success_url = reverse_lazy('payroll:employee_list')
    fields  ='__all__'
