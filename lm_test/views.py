from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm
# Create your views here.

# Index View/Search View
def index(request):
    """ Takes you back to the home page """
    return render(request, 'lm_test/index.html')

# Search
# Submit Search Form
# If form is valid then search NCBI Database
# Stick results into variables
# Display Results

# def get_results(request):
#     if request.method == "GET":
#         form = SearchForm(request.GET)
#         if form.is_valid():

#             return HttpResponseRedirect('/thanks/')
#     else:
#         form = SearchForm()
#     return render(request, 'search.html', {'form',form})