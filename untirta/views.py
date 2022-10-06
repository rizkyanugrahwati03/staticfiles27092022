from django.shortcuts import render 
from django.template import loader

def index(request):
    context = {
        'judul':'Universitas Sultan Ageng Tirtayasa',
    }
    return render(request,'index.html',context)