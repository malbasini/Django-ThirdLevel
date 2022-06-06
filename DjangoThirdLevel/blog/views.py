from django.shortcuts import render
# Create your views here.
from multiprocessing import context
from django.http import HttpResponse,HttpResponseRedirect
from .forms import BlogPostModelForm,FormRegistrazioneUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
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


def registrazione(request):
    if request.method == "POST":
        form = FormRegistrazioneUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = FormRegistrazioneUser()
    context = {"form": form}
    return render(request, "registration/registrazione.html", context)
