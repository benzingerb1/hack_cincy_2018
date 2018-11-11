from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def metronome(request):
    return render(request, 'metronome-app.html')