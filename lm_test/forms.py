from django import forms

class SearchForm(forms.Form):
    disease_name = forms.CharField(label="Disease Name", max_length=100, required="True")
    year_from = forms.DateField(label="Year From", required="True")
    year_to = forms.DateField(label="Year To", required="True")
    email = forms.EmailField(label="Email Address", required=True)
