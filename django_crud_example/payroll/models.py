from django.db import models

class Department(models.Model):
    DeptName=models.CharField(max_length=30)
    LocationName=models.CharField(max_length=30)

    def __str__(self):
        return self.DeptName
    
class Country(models.Model):
    CountryName=models.CharField(max_length=30)

    def __str__(self):
        return self.CountryName
    
class Employee(models.Model):

    COUNTRIES =[
        ("IND", "INDIA"),
        ("USA", "United States Of America"),
        ("UK", "United Kingdom"),    
        ("AUS", "AUSTRALIA"),
        ("AU", "AUSTRIA"),
        ("SP", "SPAIN"),    
        ] 
     
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    TitleName=models.CharField(max_length=30)
    HasPassport=models.BooleanField()
    Salary=models.IntegerField()
    BirthDate=models.DateField()
    HireDate=models.DateField()
    Notes=models.CharField(max_length=200)
    Email=models.EmailField(default="",max_length=50)
    PhoneNumber=models.CharField(default="",max_length=20)
    EmpDepartment=models.ForeignKey("Department",on_delete=models.PROTECT,related_name="Departments")
    EmpCountry=models.ForeignKey("Country",on_delete=models.PROTECT,related_name="Countries")