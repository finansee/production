from django.shortcuts import render, HttpResponse

# Create your views here.
def loginUser(request):
    return render(request, 'login.html')

def registerUser(request):
    return render(request, 'register.html')

def quiz(request):
    return render(request, 'quiz.html')

