from django import forms

class SearchForm(forms.Form):
    disease_name = forms.CharField(label="Disease Name", max_length=100)
    disease_area = forms.CharField(label="Disease Area", max_length=100)
    year_beginning = forms.DateField(label="Year Beginning")
    year_ending = forms.DateField(label="Year Ending")
