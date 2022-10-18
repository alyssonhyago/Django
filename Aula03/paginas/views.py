from django.shortcuts import render

# Create your views here.
def index(resquest):
    return render(resquest, 'paginas/index.html')


def sobre(resquest):
    return render(resquest, 'paginas/sobre.html')