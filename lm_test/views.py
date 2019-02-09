from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm
from Bio import Entrez
import sys, certifi, csv
# Create your views here.

# Index View/Search View
def index(request):
    """ Takes you back to the home page """
    form = SearchForm()
    context = {
        'form': form,
    }
    return render(request, 'lm_test/index.html', context)

# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=20&sort=relevance&mindate=2010/01/01&maxdate=2019/01/01&term=fever

def results(request):
    disease = request.GET.get('disease_name')
    year_from = int(request.GET.get('year_from'))
    year_to = int(request.GET.get('year_to'))

    if year_from < year_to:
       years = range(year_from, year_to, +1)
    else:
        years = range(year_from, year_to, -1)
    
    Entrez.email = "chrisgbeldam@gmail.com" #Required by NCBI

    results_file = open('temp.csv', 'w') #Open csv file
    result_writer = csv.writer(results_file, delimiter=',')
    result_writer.writerow(['Year', 'Number Of Results'])
    for year in years: #Checks the number of results for each year and then loops
        handle = Entrez.esearch(
            db="pubmed",
            sort="relevance",
            term=disease,
            mindate=year,
            maxdate=year,
            retmode="xml",
        )
        results = Entrez.read(handle) 
        results_count = results['Count'] # Total number of results for the search
        results_yearly = print(f"Number of papers in {year} is {results_count}")
        handle.close() #Close E Search
        
        result_writer.writerow([year,results_count]) # Writes out the results to csv file
        
    results_file.close()
    context = {
        'disease': disease,
        'year': year,
        'results': results,
        'results_count': results_count,
        'results_file': results_file,
        }
    return render(request, 'lm_test/results.html', context)
