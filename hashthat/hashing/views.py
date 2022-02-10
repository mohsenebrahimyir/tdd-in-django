from cgitb import text
from django.shortcuts import redirect, render
from .forms import HashForm
from .models import Hash
import hashlib
from django.http import JsonResponse


def home(request):
    if request.method == "POST":
        filled_form = HashForm(request.POST)
        if filled_form.is_valid():
            text = filled_form.cleaned_data['text']
            text_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
            try:
                Hash.objects.get(hash=text_hash)
            except Hash.DoesNotExist:
                hash = Hash()
                hash.text = text
                hash.hash = text_hash
                hash.save()
            return redirect('hash', hash=text_hash)

    form = HashForm()
    context = {'form': form}
    return render(request, 'hashing/home.html', context)


def hash(request, hash):
    hash = Hash.objects.get(hash=hash)
    context = {'hash': hash}
    return render(request, 'hashing/hash.html', context)

def quickhash(request):
    text = request.GET['text']
    return JsonResponse({'hash': hashlib.sha256(text.encode('utf-8')).hexdigest()})
