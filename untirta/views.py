from django.shortcuts import render 

def index(request):
    context = {
        'judul':'Universitas Sultan Ageng Tirtayasa',
        'subjudul':'Selamat Datang',
    }
    return render(request,'index.html',context)