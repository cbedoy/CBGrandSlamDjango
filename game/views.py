from django.shortcuts import render, render_to_responde

# Create your views here.

def home(request):
    return render_to_responde('index.html')
