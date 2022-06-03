from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormContatto
# Create your views here.

def homepage(request):
    return render(request,'formsApp/home.html')
""" def contatti(request):
    return render(request,'formsApp/contatto.html')
 """
def contatti(request):
    if request.method == 'POST':
        form = FormContatto(request.POST)
        if form.is_valid():
            print('Il Form è valido!')
            print('Nome:' , form.cleaned_data['nome'])
            print('Cognome:' , form.cleaned_data['cognome'])
            print('Email:' , form.cleaned_data['email'])
            print('Contenuto:' , form.cleaned_data['contenuto'])
            return HttpResponse('<h1> Grazie per averci contattato! </h1>')
    else:
        form = FormContatto()
    context = {'form':form}
    return render(request,'formsApp/contatto.html',context)

