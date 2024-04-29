from django.db import models

# Create your models here.
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