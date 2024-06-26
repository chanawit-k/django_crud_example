# Generated by Django 5.0.4 on 2024-04-29 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0002_country_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='EmpCountry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Countries', to='payroll.country'),
        ),
        migrations.AddField(
            model_name='employee',
            name='EmpDepartment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Departments', to='payroll.department'),
        ),
    ]
