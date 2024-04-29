from django.contrib.auth.views import logout_then_login
from django.urls import path
from . import views

app_name = 'payroll'


urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employee_list'),
    path("<int:pk>/", views.EmployeeDetailView.as_view(), name="employee_detail"),
    path("delete/<int:pk>/", views.EmployeeDeleteView.as_view(), name="employee_delete"),
    path("update/<int:pk>/", views.EmployeeUpdateView.as_view(), name="employee_update"),
    path("create/", views.EmployeeCreateView.as_view(), name="employee_create"),
]