from django.shortcuts import render

# Create your views here.

def teste(resquest):
    return render(resquest, 'sobre/index.html')