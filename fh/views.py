from django.shortcuts import render

# Create your views here.
def prodi3(request):
    judulfh = ["Ilmu Hukum"]

    konteks = {
        'titlefh' : judulfh,
        
    }
    return render(request, 'fh/index.html', konteks)

from . models import Dosen, Mahasiswa, Tendik
# Create your views here.
def prodi3(request):
    dosen = Dosen.objects.all()
    tendik = Tendik.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'dataDosen': dosen,
        'dataTendik': tendik,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'fh/index.html', konteks)
