from django.shortcuts import render

# Create your views here.
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .forms import BlogPostModelForm
# Create your views here.

def creaPostView(request):
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST)
        if form.is_valid():
            print('Il Form è valido!')
            new_post = form.save()
            return HttpResponse('<h1> Post creato con successo! </h1>')
    else:
        form = BlogPostModelForm()
    context = {'form':form}
    return render(request,'blog/createpost.html',context)