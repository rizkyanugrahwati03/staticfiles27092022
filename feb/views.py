from django.shortcuts import render

# Create your views here.
def prodi2(request):
    judulfeb = ["Sarjana Managemen", "Sarjana Akuntansi", "Sarjana Ilmu Ekonomi Pembangunan", "Sarjana Ekonomi Syariah", "Diploma III Akuntansi", "Diploma III Marketing", "Diploma III Perpajakan", "Diploma III Keuangan Perbankan"]
    
    konteks = {
        'titlefeb' : judulfeb,
        
    }
    return render(request, 'feb/index.html', konteks)