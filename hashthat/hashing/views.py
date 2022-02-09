from multiprocessing import context
from django.shortcuts import render
from .forms import HashForm
 

def home(request):
    form = HashForm()
    context = {
        'form': form,
    }
    return render(request, 'hashing/home.html', context)
