from django import forms
from .models import District, Branch, AccountType

class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female'), ('O', 'Other')))
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    district = forms.ModelChoiceField(queryset=District.objects.all(), empty_label="Select district", widget=forms.Select(attrs={'onChange': 'load_branches();'}))
    branch = forms.ModelChoiceField(queryset=Branch.objects.none(), empty_label="Select branch", widget=forms.Select())
    account_type = forms.ModelChoiceField(queryset=AccountType.objects.all())
    materials = forms.MultipleChoiceField(choices=(('Cheque book', 'Cheque book'), ('ATM card', 'ATM card'), ('Passbook', 'Passbook')), widget=forms.CheckboxSelectMultiple)
