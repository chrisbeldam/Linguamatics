from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Index View/Search View
def index(request):
    """ Takes you back to the home page """
    return render(request, 'lm_test/index.html')