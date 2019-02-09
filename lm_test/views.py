from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm
from Bio import Entrez
import sys
import certifi
# Create your views here.

# Index View/Search View
def index(request):
    """ Takes you back to the home page """
    form = SearchForm()
    context = {
        'form': form,
    }
    return render(request, 'lm_test/index.html', context)

# Search
# Submit Search Form
# If form is valid then search NCBI Database by name or area
#Between min and max dates
# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=20&sort=relevance&mindate=2010/01/01&maxdate=2019/01/01&term=fever
# Stick results into variables
# Display Results

def results(request):
    disease = request.GET.get('disease_name')
    year_beginning = request.GET.get('year_beginning')
    year_ending = request.GET.get('year_ending')
    Entrez.email = "chrisgbeldam@gmail.com"
    handle = Entrez.esearch(
        db="pubmed",
        sort="relevance",
        term=disease,
        mindate=year_beginning,
        maxdate=year_ending,
        retmode="xml",
    )
    results = Entrez.read(handle)
    handle.close()
    print(results)
    context = {
        'results': results,
        }
    return render(request, 'lm_test/results.html', context)
