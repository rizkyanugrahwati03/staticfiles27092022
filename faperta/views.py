from django.shortcuts import render

# Create your views here.
def prodi1(request):
    judulfaperta = ["Agribisnis", "Agroekoteknologi", "Ilmu Perikanan", "Teknologi Pangan"]
    
    konteks = {
        'titlefaperta' : judulfaperta,
        
    }
    return render(request, 'faperta/index.html', konteks)

