from django.shortcuts import render

# Create your views here.
def prodi4(request):
    judulfisip = ["Administrasi Publik", "Ilmu Komunikasi", "Ilmu Pemerintahan"]

    konteks = {
        'titlefisip' : judulfisip,
        
    }
    return render(request, 'fisip/index.html', konteks)

from . models import Dosen, Mahasiswa, Tendik

# Create your views here.
def prodi4(request):
    dosen = Dosen.objects.all()
    tendik = Tendik.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'dataDosen': dosen,
        'dataTendik': tendik,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'fisip/index.html', konteks)
