from django.shortcuts import render
from . models import Dosen, Mahasiswa, Tendik

# Create your views here.
def prodi1(request):
    judulfaperta = ["Agribisnis", "Agroekoteknologi", "Ilmu Perikanan", "Teknologi Pangan"]
    dosen = Dosen.objects.all()
    tendik = Tendik.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'titlefaperta' : judulfaperta,
        'dataDosen': dosen,
        'dataTendik': tendik,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'faperta/index.html', konteks)
    

