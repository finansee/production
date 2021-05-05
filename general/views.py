from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')

def findacoach(request):
    return render(request, 'findcoach.html')

def becomeacoach(request):
    return render(request, 'coachapplication.html')