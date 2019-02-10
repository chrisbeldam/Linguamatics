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

def results(request):
    disease = request.GET.get('disease_name')
    year_from = int(request.GET.get('year_from'))
    year_to = int(request.GET.get('year_to'))

    #Increase or decrease results based on which way years are
    if year_from < year_to:
       years = range(year_from, year_to, +1)
    else:
        years = range(year_from, year_to, -1)
    
    Entrez.email = "chrisgbeldam@gmail.com" #Required by NCBI

    results_file = open('lm_test/static/lm_test/temp.csv', 'w+') #Open csv file
    result_writer = csv.writer(results_file, delimiter=',')
    result_writer.writerow(['Year', 'Count'])
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
        # results_yearly = print(f"Number of papers in {year} for {disease} is {results_count}") #printing results
        handle.close() #Close E Search
        
        result_writer.writerow([year,results_count]) # Writes out the results to csv file
        
    results_file.close()
    context = {
        'disease': disease, #Pass disease name
        'year': year, #Pass Years
        'results': results, #Pass all results
        'results_count': results_count, #Pass results count
        'results_file': results_file, #Pass results csv
        'results_yearly': results_yearly, #Pass results year
        }
    return render(request, 'lm_test/results.html', context)
