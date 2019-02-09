from django import forms

class SearchForm(forms.Form):
    disease_name = forms.CharField(label="Disease", max_length=100, required="True")
    year_beginning = forms.DateField(label="Year Beginning", required="True")
    year_ending = forms.DateField(label="Year Ending", required="True")
