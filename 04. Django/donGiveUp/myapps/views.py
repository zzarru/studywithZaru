from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    
    info ={
        
        'name' : 'aiden',
        'age' : 20
        
    }
    return render(request, 'myapps/index.html', {'info' : info})

def greeting(request):
    
    foods = ['hamburger', 'pizza', 'chicken']
    info = {
        
        'name' : 'Alice'
    }
    
    
    return render(request, 'myapps/greeting.html', {'name': 'Alice'})