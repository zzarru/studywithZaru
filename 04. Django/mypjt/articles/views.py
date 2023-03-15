from django.shortcuts import render
import random

# Create your views here.
def hahaha(request):
    
    msg = "하하하"
    
    return render(request, 'articles/qwer.html', {'data' : msg})

def hohoho(request):
    
    msg = "호호호"
    
    return render(request, 'articles/asdf.html', {'da': msg})