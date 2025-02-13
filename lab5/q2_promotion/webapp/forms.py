from django import forms

class EmployeePromotionForm(forms.Form):
    employee_id_choices = [
        ('E01', 'Employee 1'),
        ('E02', 'Employee 2'),
        ('E03', 'Employee 3'),
    ]
    employee_id = forms.ChoiceField(choices=employee_id_choices, label="Employee ID")
    doj = forms.CharField(max_length=100, label='Date of Joining')
